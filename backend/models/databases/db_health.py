from mongoengine import *

connect('foodiet')


class Weight(Document):
    date = StringField(
        required=True
    )
    user_id = ObjectIdField(
        required=True
    )
    weight = StringField(
        required=True
    )


class Food(Document):
    date = StringField(
        required=True
    )
    user_id = ObjectIdField(
        required=True
    )
    breakfast = ListField()
    lunch = ListField()
    dinner = ListField()