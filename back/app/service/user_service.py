from app.domain.user.user_repository import UserRepository
from app.domain.user.user import Users
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt, set_access_cookies, unset_jwt_cookies, create_refresh_token
from flask import jsonify
import re
class UserService:
    def __init__(self):
        self.repo = UserRepository()

    # def signup(self, **kwargs):
    #     try:
    #         user = User(**kwargs)
    #         response_user = self.repo.create_user(user)
    #         return {
    #             'id': response_user.id,
    #             'name': response_user.name,
    #             'nickname': response_user.nickname
    #         }
        # except Exception as e:
        #     raise e
    def get_allUser(self, **kwargs):
        try:
            users = self.repo.find_users()
            all_user = [{"id": user.id, "username": user.username, "email": user.email, "password": user.password} for user in users]
            return all_user
        except Exception as e:
            raise e
    def signup(self, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        email = kwargs['email'].lower()

        users = self.repo.find_users()
        lst_users = [{"id": user.id, "username": user.username, "email": user.email, "password": user.password} for user in users]

        if(len(list(filter(lambda x: x["email"] == email, lst_users))) == 1):
            return {
                "error": "User already exist"
                }
        if not re.match(r"[\w\._]{5,}@\w{3,}.\w{2,4}", email):
            return {
                "error": "not a email form"
            }
        if username and password and email:
            try:
                user = Users(**kwargs)
                self.repo.create_user(user)
                response = {
                    "content": '등록 성공'
                }
                return response
            except Exception as e:
                print(e)
                raise e
        else:
            response = {
                "content": '등록 실패'
            }
            return response
    def delete_user(self, **kwargs):
        uid = kwargs['id']
        print(uid)
        if uid:
            try:
                self.repo.remove_user(uid)
                response = {
                    'content': '삭제 성공'
                }
                return response
            except Exception as e:
                raise e
        else:
            response = {
                'content': '해당 아이디로 등록된 유저가 없습니다.'
            }
            return response
    def login(self, **kwargs):
        email = kwargs['email']
        password = kwargs['password']

        if email and password:
            try:
                users = self.repo.find_users()
                lst_users = [{"id": user.id, "username": user.username, "email": user.email, "password": user.password} for user in users]
                user = list(filter(lambda x: x["email"] == email and x["password"] == password, lst_users))
                if len(user) == 1:
                    access_token = create_access_token(identity=user[0]["id"])
                    refresh_token = create_refresh_token(identity=user[0]["id"])
                    response = jsonify(access_token=access_token, refresh_token=refresh_token)
                    set_access_cookies(response, access_token)
                    return response
                else:
                    return {
                        "error" : "Invalid"
                    }
            except Exception as e:
                raise e
        else:
            return {
                "error": "Invalid form"
            }
            
