from flask import request, jsonify
import app
from mongoengine.queryset.visitor import Q
from models.databases.db_health import Weight, Food
from models.databases.db_auth import User


class HealthWeight(object):
    @staticmethod
    def add():
        email = app.get_jwt_identity()["email"]
        date = request.form["date"]
        weight = request.form["weight"]

        user_object = User.objects(email=email).first()
        weight_object = Weight.objects(Q(date=date) & Q(user_id=user_object.pk))
        if len(weight_object) == 0:
            Weight(
                date=date,
                user_id=user_object.pk,
                weight=weight
            ).save()
        else:
            weight_object = Weight.objects(Q(date=date) & Q(user_id=user_object.pk)).first()
            weight_object.weight = weight
            weight_object.save()

        user_object.now_weight = weight
        user_object.save()

        return jsonify({
            "success": True,
            "msg": "refresh or add your daily weight successfully!!"
        }), 200

    @staticmethod
    def get():
        email = app.get_jwt_identity()["email"]
        date = request.form["date"]

        user_object = User.objects(email=email).first()
        weight_object = Weight.objects(Q(date=date) & Q(user_id=user_object.pk)).first()

        return jsonify({
            "success": True,
            "weight": weight_object.weight
        }), 200


class Meal(object):
    @staticmethod
    def add():
        email = app.get_jwt_identity()["email"]
        date = request.form["date"]
        type = request.form["type"]     # breakfast, lunch, dinner
        food_id = request.form["food_id"]

        user_object = User.objects(email=email).first()
        meal_object = Food.objects(Q(date=date) & Q(user_id=user_object.pk))

        if len(meal_object) == 0:
            if type == "breakfast":
                Food(
                    date=date,
                    user_id=user_object.pk,
                    breakfast=[food_id]
                )
            elif type == "lunch":
                Food(
                    date=date,
                    user_id=user_object.pk,
                    lunch=[food_id]
                )
            elif type == "dinner":
                Food(
                    date=date,
                    user_id=user_object.pk,
                    dinner=[food_id]
                )
        else:
            meal_object = Food.objects(Q(date=date) & Q(user_id=user_object.pk)).first()

            if type == "breakfast":
                meal_object.breakfast.append(food_id).save()
            elif type == "lunch":
                meal_object.lunch.append(food_id).save()
            elif type == "dinner":
                meal_object.dinner.append(food_id).save()

        return jsonify({
            "success": True,
            "msg": "Meal Add successfully!!"
        }), 200

    @staticmethod
    def get():
        email = app.get_jwt_identity()["email"]
        date = request.form["date"]

        user_object = User.objects(email=email).first()
        meal_object = Food.objects(Q(date=date) & Q(user_id=user_object.pk))

        if len(meal_object) == 0:
            return jsonify({
                "success": True,
                "breakfast": [],
                "lunch": [],
                "dinner": []
            }), 200
        else:
            meal_object = Food.objects(Q(date=date) & Q(user_id=user_object.pk)).first()

            return jsonify({
                "success": True,
                "breakfast": meal_object.breakfast,
                "lunch": meal_object.lunch,
                "dinner": meal_object.dinner
            }), 200
