from mongoengine import *

connect('foodiet')


class Favorite(Document):
    user_id = ObjectIdField()
    food = ListField()