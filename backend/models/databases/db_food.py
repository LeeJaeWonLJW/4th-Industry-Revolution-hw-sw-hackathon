from mongoengine import *

connect('foodiet')

class Food(Document):
    barcode = StringField()
    name = StringField()

    kcal = StringField()
    carbohydrate = StringField()
    sugar = StringField()
    protein = StringField()
    fat = StringField()
    saturated_fat = StringField()
    monounsaturated_fat = StringField()
    calcium = StringField()
    sodium = StringField()
    cholesterol = StringField()