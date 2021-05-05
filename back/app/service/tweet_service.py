from app.domain.twitter.twitter_repository import TweetRepository
from app.domain.twitter.twitter import Tweet 
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt, set_access_cookies, unset_jwt_cookies, create_refresh_token
from flask import jsonify
import re

class TweetService:
    def __init__(self):
        self.repo = TweetRepository()

    def getTweets(self):
        tweets = self.repo.find_tweets()
        return [{"id": tweet.id, "title": tweet.title, "content": tweet.content, "user": self.repo.getUser(tweet.uid)} for tweet in tweets]

    def postTweets(self, **kwargs):
        try:
            title = kwargs['title']
            content = kwargs['content']
            uid = kwargs['uid']
            self.repo.addTweet(title, content, uid)
            return jsonify({"success": "true"})
        except Exception as e:
            print(e)
            raise e
            
    def delTweet(self, tid):
        try:
            self.repo.delete_tweet(tid)
            return True
        except:
            raise e