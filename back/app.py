from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import re
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt, set_access_cookies, unset_jwt_cookies, create_refresh_token


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitter.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'this is secret'
app.config["JWT_COOKIE_SECURE"] = False
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
CORS(app)
jwt = JWTManager(app)
db = SQLAlchemy(app)

@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True) # primary_key makes it so that this value is unique and can be used to identify this record.
    username = db.Column(db.String(24), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

@app.route("/api/user", methods=["GET"])
def get_user_data():
    users = Users.query.all()
    all_user = [{"id": user.id, "username": user.username, "email": user.email, "password": user.password} for user in users]
    response = jsonify(all_user)
    status = 200
    return response, status

@app.route("/api/user", methods=["POST"])
def append_user():
    try:
        username = request.json["username"]
        password = request.json["password"]
        email = request.json["email"]
        if username and password and email:
            try:
                user = Users(username, email, password)
                db.session.add(user)
                db.session.commit()
                status = 200
                response = {
                    "content": '등록 성공'
                }
            except Exception:
                response = {
                    'content': '등록 실패'
                }
                status = 500
            finally: 
                return response, status
        else:
            response = {
                    'content': 'check your username, password, and an email'
            }
            status = 500
            return response, status
    except Exception:
        response = {
            'content': '등록 실패'
        }
        status = 500
        return response, status

@app.route("/api/user", methods=["DELETE"])
def remove_user():
    try:
        uid = request.json["id"]
        print(uid)
        if (uid):
            try:
                user = Users.query.get(uid) 
                db.session.delete(user) 
                db.session.commit()
                response = {
                    'content': 'Successfully deleted user from a collection' 
                }
                status = 200
            except Exception as e:
                response = {
                     'content': e
                }
                status = 500
            finally:
                return response, status
        else:
            return jsonify({"error": "Invalid form"})
    except:
        return ({"error": "Invalid form"})

def getUsers():
    users = Users.query.all()
    return [{"id": user.id, "username": user.username, "email": user.email, "password": user.password} for user in users]

def getUser(uid):
    users = Users.query.all()
    user = list(filter(lambda x: x.id == uid, users))[0]
    return {"id": user.id, "username": user.username, "email": user.email, "password": user.password}

def add_user(username, email, password):
    try:
        if username and password and email:
            try:
                user = Users(username, email, password)
                db.session.add(user)
                db.session.commit()
                status = 200
                response = {
                    "content": '등록 성공'
                }
            except Exception:
                response = {
                    'content': '등록 실패'
                }
                status = 500
            finally: 
                return response, status
        else:
            response = {
                    'content': 'check your username, password, and an email'
            }
            status = 500
            return response, status
    except Exception:
        response = {
            'content': '등록 실패'
        }
        status = 500
        return response, status

def delete_user(id):
    if id:
        try:
            user = Users.query.get(id)
            db.session.delete(user)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    else:
        return False

@app.route("/api/login", methods=["POST"])
def login():
    try:
        email = request.json["email"]
        password = request.json["password"]
        if email and password:
            users = getUsers()
            user = list(filter(lambda x: x["email"] == email and x["password"] == password, users))
            if len(user) == 1:
                access_token = create_access_token(identity=user[0]["id"])
                refresh_token = create_refresh_token(identity=user[0]["id"])
                response = jsonify(access_token=access_token, refresh_token=refresh_token)
                set_access_cookies(response, access_token)
                return response
                # access_token = create_access_token(identity=user[0]["id"])
                # return jsonify(access_token=access_token)
            else:
                return {
                    "error":"Invalid"
                }
        else:
            return jsonify({"error": "Invalid form"})
    except Exception as e:
        print(e)
        return jsonify({"error": "Invalid form"})
@app.route("/api/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT. Just return the original respone
        return response

# @app.route("/protected", methods=["GET"])
# @jwt_required()
# def protected():
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200

@app.route("/api/register", methods=["POST"])
def register():
    try:
        email = request.json["email"]
        email = email.lower()
        password = request.json["password"]
        username = request.json["username"]
        users = getUsers()
        if(len(list(filter(lambda x: x["email"] == email, users))) == 1):
            return jsonify({"error": "User already exist"})
        if not re.match(r"[\w\._]{5,}@\w{3,}.\w{2,4}", email):
            return jsonify({"error": "not a email form"})
        response, status = add_user(username, email, password)
    except Exception:
        response = {
            "error": "Invalid format"
        }
        status = 500
    finally:
        return response, status

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey("users.id"))
    user = db.relationship('Users', foreign_keys=uid)
    title = db.Column(db.String(256))
    content = db.Column(db.String(2048))

def getTweets():
    tweets = Tweet.query.all()
    return [{"id": tweet.id, "title": tweet.title, "content": tweet.content, "user": getUser(tweet.uid)} for tweet in tweets]

def getUserTweets(uid):
    tweets = Tweet.query.all()
    return [{"id": item.id, "userid": item.user_id, "title": item.title, "content": item.content} for item in filter(lambda i: i.user_id == uid, tweets)]

def addTweet(title, content, uid):
    if title and content and uid:
        try:
            user = list(filter(lambda i: i.id == uid, Users.query.all()))[0]
            print(user)
            twt = Tweet(title=title, content=content, user=user)
            db.session.add(twt)
            db.session.commit()
            return True
        except Exception as e:
            print(e)
            return False
    else:
        return False

def delTweet(tid):
    try:
        tweet = Tweet.query.get(tid)
        db.session.delete(tweet)
        db.session.commit()
        return True
    except Exception as e:
        print(e)
        return False

@app.route("/api/tweets")
def get_tweets():
    return jsonify(getTweets())

@app.route("/api/addtweet", methods=["POST"])
# @jwt_required()
def add_tweet():
    try:
        title = request.json["title"]
        content = request.json["content"]
        uid = request.json["uid"]
        print(title, content, uid)
        addTweet(title, content, uid)
        return jsonify({"success": "true"})
    except Exception as e:
        print(e)
        return jsonify({"error": "Invalid form"})

@app.route("/api/deletetweet",methods=["DELETE"])
# @jwt_required()
def delete_tweet():
    try:
        tweetId = request.json["tid"]
        delTweet(tweetId)
        response = {
            "content": "등록 성공"
        }
        status = 200
        return response, status
    except:
        response = {
            "content": "등록 실패"
        }
        status = 500
        return response, status

# @app.route("/logout", methods=["POST"])
# def logout():
#     response = jsonify({"msg": "logout successful"})
#     unset_jwt_cookies(response)
#     return response

if __name__ == "__main__":
    app.run(debug=True)