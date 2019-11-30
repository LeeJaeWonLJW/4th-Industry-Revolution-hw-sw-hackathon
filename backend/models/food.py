import pymysql
from flask import jsonify, request
import requests
import json
import re
from models.databases import db_food


class Food(object):
    @staticmethod
    def barcode_get_id():
        barcode_data = request.form['barcode']

        barcode_object = db_food.Food.objects(barcode=barcode_data)
        if len(barcode_object) == 0:
            try:
                conn = pymysql.connect(host='localhost', user='root', password='worldstar3', db='food', charset='utf8', autocommit=True)
                curs = conn.cursor(pymysql.cursors.DictCursor)
                curs.execute("SELECT * FROM barcode WHERE BRCD_NO={}".format(barcode_data))
                data_mysql = curs.fetchall()[0]

                if data_mysql['haccp'] == 1:
                    end_point = "http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService"
                    service_key = "9drLaXi%2BzFpI1aDvx0VonbgueyKClZeM7juSYEuM6pAmOxZLvtnZwtA0%2FGSUXDrq3VuUceE7lCpj1ynTTK64hw%3D%3D"
                    res = requests.get("{}?ServiceKey={}&prdlstReportNo={}&returnType={}".format(end_point, service_key, data_mysql['PRDLST_REPORT_NO'], 'json'))
                    data = json.loads(res.text)

                    if not data['list'][0]['nutrient'] in "알수없음":
                        remover = re.compile('[ \\{\\}\\[\\]\\/?.,;:|\\)*~`!^\\-_+<>@\\#$201705484642%&\\\\=\\(\'"※]')

                        kcal = re.compile("열량[0-9]*kcal")
                        carbohydrate = re.compile("탄수화물[0-9]*g")
                        sugar = re.compile("당류[0-9]*g")
                        protein = re.compile("단백질[0-9]*g")
                        fat = re.compile("지방[0-9]*g")
                        saturated_fat = re.compile("포화지방[0-9]*g")
                        monounsaturated_fat = re.compile("트랜스지방[0-9]*g")
                        calcium = re.compile("칼슘[0-9]*mg")
                        cholesterol = re.compile("콜레스테롤[0-9]*mg")
                        sodium = re.compile("나트륨[0,9]]*mg")

                        data = remover.sub('', data)

                        db_food.Food(
                            barcode=barcode_data,
                            name=data_mysql['list'][0]['prdlstNm'],
                            kcal=kcal.search(data).group(),
                            carbohydrate=carbohydrate.search(data).group(),
                            sugar=sugar.search(data).group(),
                            protein=protein.search(data).group(),
                            fat=fat.search(data).group(),
                            saturated_fat=saturated_fat.search(data).group(),
                            monounsaturated_fat=monounsaturated_fat.search(data).group(),
                            calcium=calcium.search(data).group(),
                            sodium=sodium.search(data).group(),
                            cholesterol=cholesterol.search(data).group()
                        ).save()
            except Exception as e:
                print(e)

        db_data = db_food.Food.objects(barcode=str(barcode_data))
        if len(db_data) == 0:
            return jsonify({
                "success": False,
                "msg": "can't find barcode in db"
            }), 200
        else:
            return jsonify({
                "success": True,
                "food_id": db_data[0].pk,
                "name": db_data[0].name,
                "kcal": db_data[0].kcal,
                "nutrient": {
                    "carbohydrate": db_data[0].carbohydrate,
                    "protein": db_data[0].protein,
                    "sugar": db_data[0].sugar,
                    "fat": db_data[0].fat,
                    "saturate_fat": db_data[0].saturated_fat,
                    "monounsaturated_fat": db_data[0].monounsaturated_fat,
                    "calcium": db_data[0].calcium,
                    "sodium": db_data[0].sodium,
                    "cholesterol": db_data[0].cholesterol
                }
            }), 200

    @staticmethod
    def search_by_name():
        name = request.form['name']

        return jsonify({
            "success": True,
            "food_id": db_food.Food.objects(name=name).first().pk
        }), 200


    @staticmethod
    def barcode_add_id():
        barcode = request.form['barcode']
        picture = request.form['picture']

        name = request.form['name']
        volume = request.form['volume']
        kcal = request.form['kcal']
        carbohydrate = request.form['carbohydrate']
        sugar = request.form['sugar']
        protein = request.form['protein']
        fat = request.form['fat']
        saturated_fat = request.form['saturated_fat']
        monounsaturated_fat = request.form['monounsaturated_fat']
        calcium = request.form['calcium']
        cholesterol = request.form['cholesterol']
        sodium = request.form['sodium']

        db_food.Food(
            barcode=barcode,
            name=name,
            kcal=kcal,
            carbohydrate=carbohydrate,
            sugar=sugar,
            protein=protein,
            fat=fat,
            saturated_fat=saturated_fat,
            monounsaturated_fat=monounsaturated_fat,
            calcium=calcium,
            sodium=sodium,
            cholesterol=cholesterol,
            volume=volume,
            picture=picture
        ).save()

        food_object = db_food.Food.objects(name=name).first()

        return jsonify({
            "success": True,
            "food_id": food_object.pk,
            "msg": "add new product successfully!!"
        }), 200

    @staticmethod
    def get_food_info():
        food_id = request.form['food_id']

        food_object = db_food.Food.objects(id=food_id)
        if len(food_object) == 0:
            return jsonify({
                "success": False,
                "msg": "Can't find this id"
            }), 200
        else:
            food_object = db_food.Food.objects(id=food_id).first()
            return jsonify({
                "success": True,
                "name": food_object.name,
                "kcal": food_object.kcal,
                "carbohydrate": food_object.carbohydrate,
                "sugar": food_object.sugar,
                "protein": food_object.protein,
                "fat": food_object.fat,
                "saturated_fat": food_object.saturated_fat,
                "monounsaturated_fat": food_object.monounsaturated_fat,
                "calcium": food_object.calcium,
                "sodium": food_object.sodium,
                "cholesterol": food_object.cholesterol,
                "volume": food_object.volume,
                "picture": food_object.picture
            }), 200
