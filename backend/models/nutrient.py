from flask import request, jsonify
from models.databases import db_nutrient
from models.error import Error
import app
import datetime
import pytz
from mongoengine.queryset.visitor import Q


class NutrientToday(object):
    def add(self):
        kcal = float(request.form['kcal'])
        carb = float(request.form['carb'])
        protein = float(request.form['protein'])
        fat = float(request.form['fat'])

        tmp = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
        start = tmp.replace(hour=0, minute=0, second=0)
        end = tmp.replace(hour=23, minute=59, second=59)
        nutrient_object = db_nutrient.Nutrient.objects(
            Q(date__gte=start) & Q(date__lte=end)
        )

        if len(nutrient_object) == 0:
            try:
                db_nutrient.Nutrient(
                    kcal=kcal,
                    carb=carb,
                    protein=protein,
                    fat=fat
                ).save()
            except:
                return Error.db_error()
        else:
            try:
                nutrient_object = nutrient_object.first()
                nutrient_object.kcal = nutrient_object.kcal + kcal
                nutrient_object.carb = nutrient_object.carb + carb
                nutrient_object.protein = nutrient_object.protein + protein
                nutrient_object.fat = nutrient_object.fat + fat
                nutrient_object.save()
            except:
                return Error.db_error()

        return jsonify({
            "success": True,
            "msg": "add nutrient Today"
        }), 200

    def lookup(self):
        tmp = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
        start = tmp.replace(hour=0, minute=0, second=0)
        end = tmp.replace(hour=23, minute=59, second=59)
        nutrient_object = db_nutrient.Nutrient.objects(
            Q(date__gte=start) & Q(date__lte=end)
        )

        if len(nutrient_object) == 0:
            return Error.cant_find()
        else:
            nutrient_object = nutrient_object.first()

            return jsonify({
                "success": True,
                "msg": "Today nutrient status lookup successfully.",
                "data": {
                    "kcal": nutrient_object.kcal,
                    "carb": nutrient_object.carb,
                    "protein": nutrient_object.protein,
                    "fat": nutrient_object.fat
                }
            }), 200