from flask import request,jsonify
import app
from models.databases.db_auth import User
from models.databases.db_favorite import Favorite


class Recommend(object):
    @staticmethod
    def add(email):
        favorite = str(request.form['favorite']).split(',')

        user_object = User.objects(email=email)
        favorite_object = Favorite.objects(user_id=user_object.pk)

        if len(favorite_object) == 0:
            Favorite(
                user_id=user_object.pk,
                food=favorite
            ).save()
        else:
            favorite_object.food.append(favorite).save()

        return jsonify({
            "success": True,
            "msg": "add my favorite food successfully"
        }), 200
