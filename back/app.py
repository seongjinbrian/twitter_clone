from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import Flask_cors import CORS
import re


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitter.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'this is secret'
CORS(app)
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True) # primary_key makes it so that this value is unique and can be used to identify this record.
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
def add_user():
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
def delete_user():
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
    return [{"id": i.id, "username": i.username, "email": i.email, "password": i.password} for i in users]

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
            return False
    else:
        return False

@app.route("/api/login", methods=["POST"])
def login():
    try:
        email = request.json["email"]
        password = request.json["password"]
        if (email and password):
            users = getUsers()
            # Check if user exists
            return jsonify(len(list(filter(lambda x: x["email"] == email and x["password"] == password, users))) == 1)
        else:
            return jsonify({"error": "Invalid form"})
    except:
        return jsonify({"error": "Invalid form"})

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

if __name__ == "__main__":
    app.run(debug=True)