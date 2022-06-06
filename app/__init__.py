from app.controllers.register import register
from app.controllers.login import login
from app.controllers.home import home
from app.controllers import *
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_jwt_extended import *
from datetime import timedelta

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = 'mysql://root:''@db2/flask'

# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{database}".format(
#     username="root",
#     password="123",
#     hostname="db2",
#     database="flask",)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config['SECRET_KEY'] = 'super secret key'
SQLALCHEMY_TRACK_MODIFICATIONS = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
app.config['JWT_SECRET_KEY'] = 'super-secret'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=30)
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_CSRF_CHECK_FORM'] = True
jwt = JWTManager(app)


def assign_access_refresh_tokens(indetity):
    access_token = create_access_token(identity=str(indetity), fresh=True)
    refresh_token = create_refresh_token(identity=str(indetity))
    resp = jsonify({'login': True})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
    return resp


# @jwt.additional_claims_loader
# def add_claims_to_access_token(indetity):
#     if indetity == "admin":
#         role = "Admin"
#     else:
#         role = "User"
#     return {
#         "role": role,
#         "name": indetity.upper(),
#     }


app.register_blueprint(home, url_prefix="/home")
app.register_blueprint(login, url_prefix="")
app.register_blueprint(register, url_prefix="/register")
