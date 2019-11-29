from mongoengine import *
import datetime
import pytz

connect('foodiet')

class Nutrient(Document):
    date = DateTimeField(
        default=datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    )
    kcal = FloatField(
        default=0.0
    )
    carb = FloatField(
        default=0.0
    )
    protein = FloatField(
        default=0.0
    )
    fat = FloatField(
        default=0.0
    )

    meta = {'auto_create_index': True}