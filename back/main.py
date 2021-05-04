from app import create_app

app = create_app()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)




# def getUsers():
#     users = Users.query.all()
#     return [{"id": user.id, "username": user.username, "email": user.email, "password": user.password} for user in users]

# def getUser(uid):
#     users = Users.query.all()
#     user = list(filter(lambda x: x.id == uid, users))[0]
#     return {"id": user.id, "username": user.username, "email": user.email, "password": user.password}


# @app.route("/api/register", methods=["POST"])
# def register():
#     try:
#         email = request.json["email"]
#         email = email.lower()
#         password = request.json["password"]
#         username = request.json["username"]
#         users = getUsers()
#         if(len(list(filter(lambda x: x["email"] == email, users))) == 1):
#             return jsonify({"error": "User already exist"})
#         if not re.match(r"[\w\._]{5,}@\w{3,}.\w{2,4}", email):
#             return jsonify({"error": "not a email form"})
#         response, status = add_user(username, email, password)
#     except Exception:
#         response = {
#             "error": "Invalid format"
#         }
#         status = 500
#     finally:
#         return response, status

# class Tweet(Base):
#     id = Column(Integer, primary_key=True)
#     uid = Column(Integer, ForeignKey("users.id"))
#     user = relationship('Users', foreign_keys=uid)
#     title = Column(String(256))
#     content = Column(String(2048))

# def getTweets():
#     tweets = Tweet.query.all()
#     return [{"id": tweet.id, "title": tweet.title, "content": tweet.content, "user": getUser(tweet.uid)} for tweet in tweets]

# def getUserTweets(uid):
#     tweets = Tweet.query.all()
#     return [{"id": item.id, "userid": item.user_id, "title": item.title, "content": item.content} for item in filter(lambda i: i.user_id == uid, tweets)]

# def addTweet(title, content, uid):
#     if title and content and uid:
#         try:
#             user = list(filter(lambda i: i.id == uid, Users.query.all()))[0]
#             print(user)
#             twt = Tweet(title=title, content=content, user=user)
#             session.add(twt)
#             session.commit()
#             return True
#         except Exception as e:
#             print(e)
#             return False
#     else:
#         return False

# def delTweet(tweetId):
#     try:
#         tweet = Tweet.query.get(tweetId)
#         session.delete(tweet)
#         session.commit()
#         return True
#     except Exception as e:
#         print(e)
#         return False

# @app.route("/api/tweets")
# def get_tweets():
#     return jsonify(getTweets())

# @app.route("/api/addtweet", methods=["POST"])
# # @jwt_required()
# def add_tweet():
#     try:
#         title = request.json["title"]
#         content = request.json["content"]
#         print(title, content)
#         uid = request.json["uid"]
#         print(title, content, uid)
#         addTweet(title, content, uid)
#         return jsonify({"success": "true"})
#     except Exception as e:
#         print(e)
#         return jsonify({"error": "Invalid form"})

# @app.route("/api/uid", methods=["GET"])
# @jwt_required()
# def add_tweets():
#     try:
#         hello = get_jwt_identity()
#         response = {"uid": hello}
#         return response, 200
#     except Exception as e:
#         print(e)
#         return jsonify({"error": "Invalid form"})

# @app.route("/api/deletetweet/<tweetId>", methods=["DELETE"])
# def delete_tweet(tweetId):
#     try:
#         delTweet(tweetId)
#         response = {
#             "content": "등록 성공"
#         }
#         status = 200
#         return response, status
#     except:
#         response = {
#             "content": "등록 실패"
#         }
#         status = 500
#         return response, status