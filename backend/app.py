import datetime

from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt_identity
from flask_jwt_extended import (jwt_required, create_access_token)
from werkzeug.debug import DebuggedApplication

from models import auth, error, user, food, recommend, health

app = Flask(__name__)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'sleeping-in-suwon'
app.config['JWT_ACCESS_TOKEN_EXOIRES'] = datetime.timedelta(days=90)
app.wsgi_app = DebuggedApplication(app.wsgi_app, True)
CORS(app)


def isValidInput(datas):
    for chk in datas:
        if request.form.get(chk) == "" or request.form.get(chk) == None:
            return False
    return True

@jwt.unauthorized_loader
def unauthorized_response(callback):
    response = {
        "success": False,
        "message": "not logged in\nunauthorized response"
    }

    return jsonify(response), 403


@jwt.invalid_token_loader
def invalid_token_loader(callback):
    response = {
        "success": False,
        "message": "not logged in\ninvalid token loaded"
    }

    return jsonify(response), 403


@app.route('/')
def hello():
    return jsonify({
        "status": True,
        "msg": "Server is running now."
    }), 200

#########################################
#   Auth
#########################################

"""
@api {post} /auth/signin Login
@apiName Login
@apiGroup Auth

@apiParam {String} email
@apiParam {String} password

@apiSuccess {Boolean} success
@apiSuccess {String} accessToken user jwt token.

@apiSuccessExample {json} Success-Response:
 HTTP/1.1 200 OK
 {
     "success": true,
     "accessToken": (jwt token)
 }

 JWT Token Identity Spec
 {
    "email": (email),
    "name": (name),
    "gender": (gender),
    "age": (age),
    "height": (height),
    "weight": (weight),
    "goal_weight": (goal_weight),
    "purpose": (purpose)
 }

@apiError {Boolean} success
@apiError {String} message

@apiErrorExample {json} Error-Response 1:
 HTTP/1.1 200 OK
 {
     "success": false,
     "message": "invalid input"
 }

 @apiErrorExample {json} Error-Response 2:
 HTTP/1.1 200 OK
 {
     "success": false,
     "message": "wrong password"
 }
"""
@app.route('/auth/signin', methods=['POST'])
def auth_signin():
    if isValidInput(['email', 'password']):
        return auth.Auth().signin()
    else:
        return error.Error().invalid_input()

"""
@api {post} /auth/signup Register
@apiName Register
@apiGroup Auth

@apiParam {String} email
@apiParam {String} password
@apiParam {String} name
@apiParam {String} gender       male or female
@apiParam {String} age
@apiParam {String} height
@apiParam {String} weight
@apiParam {String} goal_weight
@apiParam {String} purpose      lose_weight or healthy 
@apiParam {String} duration
@apiParam {File}   profile      image by png

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response:
 HTTP/1.1 200 OK
 {
     "success": true,
     "msg": "successful created new user",
     "accessToken": (jwt token)
 }

 JWT Token Identity Spec
 {
    "email": (email),
    "name": (name),
    "gender": (gender),
    "age": (age),
    "height": (height),
    "weight": (weight),
    "goal_weight": (goal_weight),
    "purpose": (purpose),
    "duration": (duration),
    "profile": (profile image)
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response:
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "invalid input"
 }
"""
@app.route('/auth/signup', methods=['POST'])
def auth_signup():
    if isValidInput(['email', 'password', 'name', 'gender', 'age', 'height', 'weight', 'goal_weight', 'purpose', 'duration', 'profile']):
        return auth.Auth().signup()
    else:
        return error.Error().invalid_input()


#########################################
#   Friend
#########################################

"""
@api {post} /user/friend/add Friend add
@apiName Friend Add
@apiGroup Friend

@apiHeader  {String}  BearerToken       user jwt token
@apiParam {String} email

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "msg": "add new friend at list"
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "invalid input"
 }
@apiErrorExample {json} Can't Find
 HTTP/1.1 200 OK
 {
    "success": false,
    "msg": "fail to find added user"
 }
"""
@app.route('/user/friend/add', methods=['POST'])
@jwt_required
def user_friend_add():
    if isValidInput(['email']):
        return user.Friend().add()
    else:
        return error.Error().invalid_input()

"""
@api {post} /user/friend/search Friend search
@apiName Friend Search
@apiGroup Friend

@apiHeader  {String}  BearerToken       user jwt token
@apiParam {String} email

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "data": {
        "name": (name),
        "profile": (profile)
     }
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response-1
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "invalid input"
 }

@apiErrorExample {json} Error-Response-2
 HTTP/1.1 200 OK
 {
    "success": false,
    "msg": "can't find"
 }
"""
@app.route('/user/friend/search', methods=['POST'])
@jwt_required
def user_friend_search():
    if isValidInput(['email']):
        return user.Friend().search()
    else:
        return error.Error().invalid_input()

"""
@api {get} /user/friend/lookup My Friends lookup
@apiName My Friends Lookup
@apiGroup Friend

@apiHeader  {String}  BearerToken       user jwt token

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "length": (friends list length)
     "friends": [
        {
            "name": (name),
            "profile": (profile),
            "weight": (weight),
            "goal_weight": (goal_weight),
            "now_weight": (now_weight),
            "percentage": (weight goal do percentage)%
        },
        ...
     ]
 }
"""
@app.route('/user/friend/lookup', methods=['GET'])
@jwt_required
def user_friend_lookup():
    return user.Friend().lookup()


#########################################
#   Food
#########################################
"""
@api {post} /food/search/name Search by Name
@apiName Search by Name
@apiGroup Food

@apiHeadeKr  {String}  BearerToken       user jwt token
@apiParam {String} name     food name

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "food_id": (food_id)
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "invalid input"
 }
 """
@app.route('/food/search/name', methods=['POST'])
@jwt_required
def food_search_name():
    if isValidInput(['name']):
        return food.Food().search_by_name()
    else:
        return error.Error().invalid_input()

"""
@api {post} /food/barcode/get/id Barcode based Food ID Return API
@apiName Barcode based Food ID Return API
@apiGroup Food

@apiHeader  {String}  BearerToken       user jwt token
@apiParam {String} barcode     Barcode Number

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "food_id": (food_id),
     "name": (name),
     "kcal": (kcal),
     "nutrient": {
         "carbohydrate": (carbohydrate),
         "protein": (protein),
         "sugar": (sugar),
         "fat": (fat),
         "saturate_fat": (saturated_fat),
         "monounsaturated_fat": (monounsaturated_fat),
         "calcium": (calcium),
         "sodium": (sodium),
         "cholesterol": (cholesterol)
     }
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "invalid input"
 }
@apiErrorExample {json} Error-Response-2
 HTTP/1.1 200 OK
 {
    "success": false,
    "msg": "can't find barcode in db"
 }
"""
@app.route('/food/barcode/get/id', methods=['POST'])
@jwt_required
def food_barcode_get_id():
    if isValidInput(['barcode']):
        return food.Food().barcode_get_id()
    else:
        return error.Error().invalid_input()

"""
@api {post} /food/barcode/add/id Add Food to DB
@apiName Add Food to DB
@apiGroup Food

@apiHeader  {String}  BearerToken       user jwt token
@apiParam {String} [barcode]     Barcode Number
@apiParam {String} picture      Food Picture
@apiParam {String} volume      Food volume
@apiParam {String} kcal      Food kcal
@apiParam {String} carbohydrate      Food carbohydrate
@apiParam {String} sugar      Food sugar
@apiParam {String} protein      Food protein
@apiParam {String} fat      Food fat
@apiParam {String} saturated_fat      Food saturated_fat
@apiParam {String} monounsaturated_fat      Food monounsaturated_fat
@apiParam {String} calcium      Food calcium
@apiParam {String} cholesterol      Food cholesterol
@apiParam {String} sodium      Food sodium


@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "food_id": (food_id),
     "msg": "add new product successfully!!"
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "invalid input"
 }
"""
@app.route('/food/barcode/add/id', methods=['POST'])
@jwt_required
def food_barcode_add_id():
    if isValidInput(['picture', 'name', 'volume', 'kcal', 'carbohydrate', 'sugar', 'protein', 'fat', 'saturated_fat', 'monounsaturated_fat', 'calcium', 'cholesterol', 'sodium']):
        return food.Food().barcode_add_id()
    else:
        return error.Error().invalid_input()

"""
@api {post} /food/get/info Get Food Information
@apiName Get Food Information
@apiGroup Food

@apiHeader  {String}  BearerToken       user jwt token
@apiParam {String} food_id     Food ID

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "food_id": (food_id),
     "name": (name),
     "kcal": (kcal),
     "carbohydrate": (carbohydrate),
     "protein": (protein),
     "sugar": (sugar),
     "fat": (fat),
     "saturate_fat": (saturated_fat),
     "monounsaturated_fat": (monounsaturated_fat),
     "calcium": (calcium),
     "sodium": (sodium),
     "cholesterol": (cholesterol)
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "invalid input"
 }
@apiErrorExample {json} Error-Response-2
 HTTP/1.1 200 OK
 {
    "success": false,
    "msg": "can't find this this id"
 }
"""
@app.route('/food/get/info', methods=['POST'])
@jwt_required
def food_get_info():
    if isValidInput(['food_id']):
        return food.Food().get_food_info()
    else:
        return error.Error().invalid_input()


#########################################
#   Health
#########################################

"""
@api {post} /health/weight/add Refresh/Add Today Weight
@apiName Refresh/Add Today Weight
@apiGroup Health

@apiHeader  {String}  BearerToken       user jwt token
@apiParam {String} date     20001207
@apiParam {String} weight   now weight

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "msg": "refresh or add your daily weight successfully!!"
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "invalid input"
 }
"""
@app.route('/health/weight/add', methods=['POST'])
@jwt_required
def health_weight_add():
    if isValidInput(['date', 'weight']):
        return health.HealthWeight().add()
    else:
        return error.Error().invalid_input()

"""
@api {post} /health/weight/get Get Specific Date Weight
@apiName Get Specific Date Weight
@apiGroup Health

@apiHeader  {String}  BearerToken       user jwt token
@apiParam {String} date     20001207

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "weight": (date weight)
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "invalid input"
 }
"""
@app.route('/health/weight/get', methods=['POST'])
@jwt_required
def health_weight_get():
    if isValidInput(['date']):
        return health.HealthWeight().get()
    else:
        return error.Error().invalid_input()

"""
@api {post} /health/meal/add add eat Food
@apiName add eat Food
@apiGroup Health

@apiHeader  {String}  BearerToken       user jwt token
@apiParam {String} date     20001207
@apiParam {String} type     breakfast or lunch or dinner
@apiParam {String} food_id  food_id can get Food Section API

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "msg": "Meal Add successfully!!"
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "invalid input"
 }
"""
@app.route('/health/meal/add', methods=['POST'])
@jwt_required
def health_meal_add():
    if isValidInput(['date', 'type', 'food_id']):
        return health.Meal().add()
    else:
        return error.Error().invalid_input()

"""
@api {post} /health/meal/get Get eat Food
@apiName Get eat Food
@apiGroup Health

@apiHeader  {String}  BearerToken       user jwt token
@apiParam {String} date     20001207

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "breakfast": [(food_id), ...],
     "lunch": [(food_id), ...],
     "dinner": [(food_id), ...]
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "invalid input"
 }
"""
@app.route('/health/meal/get', methods=['POST'])
@jwt_required
def health_meal_get():
    if isValidInput(['date']):
        return health.Meal().get()
    else:
        return error.Error().invalid_input()


#########################################
#   AI
#########################################

"""
@api {post} /ai/food/add Favorite Food Add
@apiName Favorite Food Add
@apiGroup AI

@apiHeader  {String}  BearerToken       user jwt token
@apiParam {String} favorite     Write with korean

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "msg": "add my favorite food successfully"
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "invalid input"
 }
"""
@app.route('/ai/food/add', methods=['POST'])
@jwt_required
def ai_food_add():
    if isValidInput(['favorite']):
        print(get_jwt_identity())
        return recommend.Recommend().add()
    else:
        return error.Error().invalid_input()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, use_reloader=True)
