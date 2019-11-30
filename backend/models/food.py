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
                    print(data_mysql['PRDLST_REPORT_NO'])
                    end_point = "http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService"
                    service_key = "9drLaXi%2BzFpI1aDvx0VonbgueyKClZeM7juSYEuM6pAmOxZLvtnZwtA0%2FGSUXDrq3VuUceE7lCpj1ynTTK64hw%3D%3D"
                    res = requests.get("{}?ServiceKey={}&prdlstReportNo={}&returnType={}".format(end_point, service_key, data_mysql['PRDLST_REPORT_NO'], 'json'))
                    print(res.text)
                    data = json.loads(res)
                    print(data)

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
"""
    @staticmethod
    def self_data_add():


    def barcode(self):
        barcode_data = request.form['barcode']
        print(barcode_data)
        try:
            conn = pymysql.connect(host='localhost', user='root', password='worldstar3', db='food', charset='utf8', autocommit=True)
            curs = conn.cursor(pymysql.cursors.DictCursor)
            curs.execute("SELECT * FROM barcode WHERE BRCD_NO={}".format(barcode_data))
            data_mysql = curs.fetchall()[0]

            if data_mysql['haccp'] == 1:
                end_point = "http://apis.data.go.kr/B553748/CertImgListService/getCertImgListService"
                service_key = "9drLaXi%2BzFpI1aDvx0VonbgueyKClZeM7juSYEuM6pAmOxZLvtnZwtA0%2FGSUXDrq3VuUceE7lCpj1ynTTK64hw%3D%3D"
                res = requests.get("{}?ServiceKey={}&prdlstReportNo={}&returnType={}".format(end_point, service_key, data_mysql['PRDLST_REPORT_NO'], 'json'))
                data = json.loads(res)

                if not data['list'][0]['nutrient'] in "알수없음":
                    remover = re.compile('[ \\{\\}\\[\\]\\/?.,;:|\\)*~`!^\\-_+<>@\\#$%&\\\\=\\(\'"※]')

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

                    return jsonify({
                        "success": True,
                        "name": data_mysql['list'][0]['prdlstNm'],
                        "kcal": kcal.search(data).group(),
                        "nutrient": {
                            "carb": carbohydrate.search(data).group(),
                            "protein": protein.search(data).group(),
                            "sugar": sugar.search(data).group(),
                            "fat": fat.search(data).group(),
                            "saturate_fat": saturated_fat.search(data).group(),
                            "monounsaturated_fat": monounsaturated_fat.search(data).group(),
                            "calcium": calcium.search(data).group(),
                            "cholesterol": cholesterol.search(data).group(),
                            "sodium": sodium.search(data).group()
                        }
                    }), 200
        except:
            pass
        db_data = db_food.Food.objects(barcode=str(barcode_data))
        return jsonify({
            "success": True,
            "name": db_data[0].name,
            "kcal": db_data[0].kcal,
            "nutrient": {
                "carb": db_data[0].carbohydrate,
                "protein": db_data[0].protein,
                "sugar": db_data[0].sugar,
                "fat": db_data[0].fat,
                "saturate_fat": db_data[0].saturated_fat,
                "monounsaturated_fat": db_data[0].monounsaturated_fat,
                "calcium": db_data[0].calcium,
                "sodium": db_data[0].sodium
            }
        }), 200
"""