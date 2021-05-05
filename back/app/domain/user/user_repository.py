from app import Session
from app.domain.user.user import Users


class UserRepository:
    def __init__(self, session=None):
        self.session = Session()

    # signup
    # def create_user(self, user, **kwargs):
    #     try:
    #         self.session.add(user)
    #         self.session.commit()
    #         return user
    #     except Exception as e:
    #         self.session.rollback()
    #         raise Exception(e)
    def find_users(self):
        try:
            users = self.session.query(Users).all()
            self.session.commit()
            return users
        except Exception as e:
            self.session.rollback()
            raise e
    def create_user(self, user, **kwargs):
        try:
            self.session.add(user)
            self.session.commit()
            return user
        except Exception as e:
            self.session.rollback()
            raise Exception(e)
    def remove_user(self, uid):
        try:
            user = self.session.query(Users).filter(Users.id == uid).first()
            self.session.delete(user)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise Exception(e)
    # def getUsers(self):
    #     users = self.session.query(Users).all()
    #     return [{"id": user.id, "username": user.username, "email": user.email, "password": user.password} for user in users]