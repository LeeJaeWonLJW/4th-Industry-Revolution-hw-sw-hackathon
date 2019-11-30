from models.databases import db_auth
from models.error import Error
from flask import jsonify, request
import app
import json
from collections import OrderedDict


class Friend(object):
    @staticmethod
    def search():
        email = str(request.form['email'])
        user_object = db_auth.User.objects(email=email)

        if len(user_object) == 0:
            return Error.cant_find()
        else:
            user_object = db_auth.User.objects(email=email).first()
            profile = user_object.profile
            name = user_object.name

            return jsonify({
                "success": True,
                "data": {
                    "name": name,
                    "profile": profile
                }
            }), 200

    @staticmethod
    def add():
        my_email = app.get_jwt_identity()["email"]
        add_email = str(request.form['email'])
        user_object = db_auth.User.objects(email=my_email)

        if len(user_object) == 0:
            return Error.invalid_input()
        else:
            add_object = db_auth.User.objects(email=add_email)
            if len(add_object) == 0:
                return jsonify({
                    "success": False,
                    "msg": "fail to find added user"
                })
            else:
                user_object = user_object.first()
                user_object.friends.append(add_email)
                user_object.save()

                return jsonify({
                    "success": True,
                    "msg": "add new friend at list"
                }), 200

    @staticmethod
    def lookup():
        my_email = app.get_jwt_identity()["email"]

        user_object = db_auth.User.objects(email=my_email).first()
        friends = user_object.friends
        response = OrderedDict()
        response["success"] = True
        response["length"] = len(friends)
        response["friends"] = []

        for friend in friends:
            friend_object = db_auth.User.objects(email=friend).first()
            response["friends"].append({
                "name": friend_object.name,
                "profile": friend_object.profile,
                "weight": friend_object.weight,
                "goal_weight": friend_object.goal_weight,
                "now_weight": friend_object.now_weight,
                "percentage": (float(friend_object.weight) - float(friend_object.now_weight)) / (float(friend_object.weight) - float(friend_object.goal_weight)) * 100.0 + "%"
            })

        return jsonify(response), 200


class Flavor(object):
    def set(self):
        flavor = eval(request.form['flavor'])
        phone = app.get_jwt_identity()["email"]
        user_object = db_auth.User.objects(email=phone).first()

        user_object.flavor = flavor
        user_object.save()

        return jsonify({
            "success": True,
            "msg": "successful set food flavor"
        })