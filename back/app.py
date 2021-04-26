from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitter.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'this is secret'

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

if __name__ == "__main__":
    app.run(debug=True)