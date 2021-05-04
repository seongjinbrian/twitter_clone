from app import Session
from app.domain.twitter.twitter import Tweet


class UserRepository:
    def __init__(self, session=None):
        self.session = Session()

    # signup