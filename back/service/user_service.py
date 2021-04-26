from domain.user.user_repository import UserRepository
from domain.user.user import User
from config.exception import UnauthorizedException

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def signup(self, **kwargs):
        try:
            user = User(**kwargs)
            response_user = self.repo.create_user(user)
            return {
                'id': response_user.id,
                'name': response_user.name,
                'nickname': response_user.nickname
            }
        except Exception as e:
            raise e