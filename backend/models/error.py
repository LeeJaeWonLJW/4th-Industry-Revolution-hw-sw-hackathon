from flask import jsonify


class Error(object):
    @staticmethod
    def invalid_input():
        return jsonify({
            "success": False,
            "msg": "invalid input"
        }), 200

    @staticmethod
    def user_not_found():
        return jsonify({
            "success": False,
            "msg": "user not found"
        }), 200

    @staticmethod
    def wrong_password():
        return jsonify({
            "success": False,
            "msg": "wrong password"
        }), 200

    @staticmethod
    def id_overlapped():
        return jsonify({
            "success": False,
            "msg": 'id overlapped'
        }), 200

    @staticmethod
    def db_error():
        return jsonify({
            "success": False,
            "msg": "db error"
        }), 200

    @staticmethod
    def cant_find():
        return jsonify({
            "success": False,
            "msg": "can't find"
        }), 200