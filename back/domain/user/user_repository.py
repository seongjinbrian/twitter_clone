from app import Session
from app.domain.user.user import User


class UserRepository:
    def __init__(self, session=None):
        self.session = Session()

    # signup
    def create_user(self, user, **kwargs):
        try:
            self.session.add(user)
            self.session.commit()
            return user
        except Exception as e:
            self.session.rollback()
            raise Exception(e)