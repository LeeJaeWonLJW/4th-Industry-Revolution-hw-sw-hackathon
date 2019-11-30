import datetime

from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt_identity
from flask_jwt_extended import (jwt_required, create_access_token)
from werkzeug.debug import DebuggedApplication

from models import auth, error, nutrient, user, food, recommend

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

"""
@apiDeprecated Developing
@api {post} /user/flavor/set Flavor Set
@apiName Flavor Set
@apiGroup User

@apiHeader  {String}  BearerToken       user jwt token
@apiParam {String} flavor

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "msg": "successful set food flavor"
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
@jwt_required
@app.route('/user/flavor/set', methods=['POST'])
def user_flavor_set():
    if isValidInput(['flavor']):
        print(get_jwt_identity())
        return user.Flavor().set()
    else:
        return error.Error().invalid_input()


"""
@apiDeprecated Developing
@api {post} /nutrient/today/add Today-Add
@apiName Today-Add
@apiGroup Nutrient

@apiHeader  {String}  BearerToken       user jwt token

@apiParam {float} kcal
@apiParam {float} carb      carbohydrate
@apiParam {float} protein
@apiParam {float} fat

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "msg": "add nutrient Today"
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response:
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "db error"
 }
"""
@jwt_required
@app.route('/nutrient/today/add', methods=['POST'])
def nutrient_today_add():
    if isValidInput(['kcal', 'carb', 'protein', 'fat']):
        return nutrient.NutrientToday().add()
    else:
        return error.Error().invalid_input()


"""
@apiDeprecated Developing
@api {post} /nutrient/today/lookup Today-Lookup
@apiName Today-Lookup
@apiGroup Nutrient

@apiHeader  {String}  BearerToken       user jwt token

@apiSuccess {Boolean} success
@apiSuccess {String} msg

@apiSuccessExample {json} Success-Response
 HTTP/1.1 200 OK
 {
     "success": true,
     "data": {
        "carb": 87,
        "fat": 0,
        "kcal": 345,
        "protein": 0
     },
     "msg": "Today nutrient status lookup successfully.",
 }

@apiError {Boolean} success
@apiError {String} msg

@apiErrorExample {json} Error-Response
 HTTP/1.1 200 OK
 {
     "success": false,
     "msg": "can't find"
 }
"""
@jwt_required
@app.route('/nutrient/today/lookup', methods=['POST'])
def nutrient_today_lookup():
    return nutrient.NutrientToday().lookup()



@jwt_required
@app.route('/food/barcode', methods=['POST'])
def food_barcode():
    if isValidInput(['barcode']):
        return food.Food().barcode()
    else:
        return error.Error().invalid_input()

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
