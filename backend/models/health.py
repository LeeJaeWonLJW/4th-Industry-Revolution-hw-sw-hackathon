from flask import request, jsonify
import app
from mongoengine.queryset.visitor import Q
from models.databases.db_health import Weight
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


class HealthFood(object):
    @staticmethod
    def add():
        email = app.get_jwt_identity()["email"]
        date = request.form["date"]
        type = request.form["type"]     # breakfast, lunch, dinner
        food_id = request.form["food_id"]
        # TODO:: id 발급 작업 후 마무리.
