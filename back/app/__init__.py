from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_cors import CORS
import re
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt, set_access_cookies, unset_jwt_cookies, create_refresh_token
from datetime import datetime, timedelta, timezone

#DB connection
engine = create_engine('sqlite:///twitter.db')

#Session
Session = scoped_session(sessionmaker(autocommit=False, bind=engine))

# app = Flask(__name__)
# jwt = JWTManager(app)
def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 512 * 1024 * 1024
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///twitter.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'this is secret'
    app.config["JWT_COOKIE_SECURE"] = False
    app.config["JWT_TOKEN_LOCATION"] = ["cookies"]

    CORS(app)

    app.config["JWT_SECRET_KEY"] = "super-secret"
    jwt = JWTManager(app)

    #router
    from app.router.user_router import user_bp
    # from app.router.twitter_router import twitter_bp

    app.register_blueprint(user_bp, url_prefix=f'/api/user')
    # app.register_blueprint(twitter_bp, url_prefix=f'/api/twitter')
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
            
    return app
