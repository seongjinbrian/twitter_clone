from flask import request, Flask, request, jsonify, Blueprint
from app.service.tweet_service import TweetService
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt, set_access_cookies, unset_jwt_cookies, create_refresh_token

tweet_service = TweetService()
tweet_bp = Blueprint('tweet', __name__)

@tweet_bp.route('', methods=["GET"])
def get_tweets():
    try: 
        response = jsonify(tweet_service.getTweets())
        status = 200
    except Exception as e:
        print(e)
        response = {
            'content': 'failed'
        }
        status = 500
    return response, status

@tweet_bp.route("/add", methods=["POST"])
# @jwt_required()
def add_tweet():
    user_info = request.get_json()
    try:
        response = tweet_service.postTweets(**user_info)
        status = 200
    except:
        response = {
            "error": "Invalid form"
        }
        status = 500
    return response,status

@tweet_bp.route("/uid", methods=["GET"])
@jwt_required()
def add_tweets():
    try:
        hello = get_jwt_identity()
        response = {"uid": hello}
        return response, 200
    except Exception as e:
        print(e)
        return jsonify({"error": "Invalid form"})

@tweet_bp.route("/delete/<tweetId>", methods=["DELETE"])
def delete_tweet(tweetId):
    try:
        tweet_service.delTweet(tweetId)
        response = {
            "content": "삭제 성공"
        }
        status = 200
        return response, status
    except:
        response = {
            "content": "삭제 실패"
        }
        status = 500
        return response, status