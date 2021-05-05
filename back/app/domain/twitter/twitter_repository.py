from app import Session
from app.domain.twitter.twitter import Tweet
from app.domain.user.user import Users

class TweetRepository:
    def __init__(self, session=None):
        self.session = Session()

    # signup
    def find_tweets(self):
        all_tweets = self.session.query(Tweet).all()
        return all_tweets
    def getUser(self, uid):
        users = self.session.query(Users).all()
        user = list(filter(lambda x: x.id == uid, users))[0]
        return {"id": user.id, "username": user.username, "email": user.email, "password": user.password}

    def addTweet(self, title, content, uid):
        try:
            users = self.session.query(Users).all()
            user = list(filter(lambda x: x.id == uid, users))[0]
            print(user)
            twt = Tweet(title=title, content=content, user=user)
            self.session.add(twt)
            self.session.commit()
            return twt
        except Exception as e:
            self.session.rollback()
            raise Exception(e)
    def delete_tweet(self, tid):
        try:
            tweet = self.session.query(Tweet).filter(Tweet.id == tid).first()
            self.session.delete(tweet)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise Exception(e)


