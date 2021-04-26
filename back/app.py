from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

Base = SQLAlchemy(app)

class Users(Base.Model):
    id = Base.Column('student_id', Base.Integer, primary_key = True)
    name = Base.Column(Base.String(24))
    email = Base.Column(Base.String(64))
    passwordd = Base.Column(Base.String(64))

    # Constructor
    def __init__(self, username, email, pwd):
        self.username = username
        self.email = email
        self.password = pwd

@app.route('/')
def index():
    return "Hello, world!"

if __name__ == "__main__":
    app.run(debug=True)