from models.databases import db_auth
from models.error import Error
from flask import jsonify, request
import app
import json


class Friend(object):
    def search(self):
        phone = str(request.form['phone'])
        user_object = db_auth.User.objects(email=phone)

        if len(user_object) == 0:
            return Error.cant_find()
        else:
            return jsonify({
                "success": True,
                "msg": "I can find your friend at the data."
            }), 200

    def add(self):
        my_phone = app.get_jwt_identity()["email"]
        friend_phone = str(request.form['phone'])
        user_object = db_auth.User.objects(email=my_phone)

        if len(user_object) == 0:
            return Error.invalid_input()
        else:
            user_object = user_object.first()
            user_object.friends.append(friend_phone)
            user_object.save()

            return jsonify({
                "success": True,
                "msg": "add new friend at list"
            }), 200


class Flavor(object):
    def set(self):
        flavor = eval(request.form['flavor'])
        phone = app.get_jwt_identity()["email"]
        user_object = db_auth.User.objects(email=phone).first()

        user_object.flavor = flavor
        user_object.save()

        return jsonify({
            "success": True,
            "msg": "successfsudo ul set food flavor"
        })