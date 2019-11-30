from mongoengine import *

connect('foodiet')


class User(Document):
    email = StringField(
        required=True,
        unique=True
    )
    password = StringField(
        required=True
    )
    name = StringField(
        required=True
    )
    gender = StringField(
        required=True
    )
    age = StringField(
        required=True
    )
    height = StringField(
        required=True
    )
    weight = StringField(
        required=True
    )
    goal_weight = StringField(
        required=True
    )
    purpose = StringField(
        required=True
    )
    duration = StringField(
        required=True
    )
    profile = StringField(
        required=True
    )

    friends = ListField()
    flavor = ListField()
    money = IntField(
        default=10000
    )

    meta = {'auto_create_index': True}