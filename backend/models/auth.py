from base64 import b64encode

from flask import request, jsonify

import app
from models.databases import db_auth
from models.error import Error
from setting import Img


class Auth(object):
    def signin(self):
        email = str(request.form['email'])
        password = str(request.form['password'])
        user_object = db_auth.User.objects(email=email)

        if len(user_object) == 0:
            return Error.invalid_input()
        else:
            if app.bcrypt.check_password_hash(eval(user_object[0].password), password):
                return jsonify({
                    "success": True,
                    "accessToken": app.create_access_token(identity={
                        "email": user_object[0].email,
                        "name": user_object[0].name,
                        "gender": user_object[0].gender,
                        "age": user_object[0].age,
                        "height": user_object[0].height,
                        "weight": user_object[0].weight,
                        "goal_weight": user_object[0].goal_weight,
                        "now_weight": user_object[0].now_weight,
                        "purpose": user_object[0].purpose,
                        "duration": user_object[0].duration
                    })
                }), 200
            else:
                return Error.wrong_password()

    def signup(self):
        try:
            email = str(request.form['email'])
            password = str(app.bcrypt.generate_password_hash(request.form['password']))
            name = str(request.form['name'])
            gender = str(request.form['gender'])
            age = str(request.form['age'])
            height = str(request.form['height'])
            weight = str(request.form['weight'])
            goal_weight = str(request.form['goal_weight'])
            purpose = str(request.form['purpose'])
            duration = str(request.form['duration'])
            profile = str(request.form['profile'])

            db_auth.User(
                email=email,
                password=password,
                name=name,
                gender=gender,
                age=age,
                height=height,
                weight=weight,
                goal_weight=goal_weight,
                now_weight=weight,
                purpose=purpose,
                duration=duration,
                profile=profile
            ).save()

            return jsonify({
                "success": True,
                "msg": "successful created new user",
                "accessToken": app.create_access_token(identity={
                    "email": email,
                    "name": name,
                    "gender": gender,
                    "age": age,
                    "height": height,
                    "weight": weight,
                    "goal_weight": goal_weight,
                    "purpose": purpose,
                    "duration": duration
                })
            }), 200
        except Exception as e:
            print(e)
            return Error.id_overlapped()