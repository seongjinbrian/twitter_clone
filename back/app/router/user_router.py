from flask import request, Flask, request, jsonify, Blueprint
from app.service.user_service import UserService
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt, set_access_cookies, unset_jwt_cookies, create_refresh_token

user_service = UserService()
user_bp = Blueprint('user', __name__)

# @user_bp.route('', methods=['POST'])
# def login():

@user_bp.route('', methods=["GET"])
def get_user_data():
    try:
        # users = user_service.get_allUser()
        # all_user = [{"id": user.id, "username": user.username, "email": user.email, "password": user.password} for user in users]
        response = jsonify(user_service.get_allUser())
        status = 200
    except Exception as e:
        print(e)
        response = {
            'content': "failed"
        }
        status = 500
    return response, status

@user_bp.route('/register', methods=["POST"])
def sign_up():
    user_info = request.get_json()
    try:
        response = user_service.signup(**user_info)
        status = 200
    except Exception as e:
        print(e)
        response = {
            'content': 'Signup failed'
        }
        status = 500
    return response, status

@user_bp.route('', methods=["DELETE"])
def remove_user():
    user_info = request.get_json()
    try:
        response = user_service.delete_user(**user_info)
        print('hi')
        status = 200
    except Exception as e:
        print(e)
        response = {
            'content': 'cannot remove user from collection'
        }
        status = 500
    return response, status

@user_bp.route('/login', methods=["POST"])
def login():
    user_info = request.get_json()
    try:
        response = user_service.login(**user_info)
        status = 200
    except Exception as e:
        response = {
            'error': 'login failed'
        }
        status = 500
    return response, status
@user_bp.route('/logout', methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response

