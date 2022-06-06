from flask import render_template, request, jsonify, Blueprint, redirect, url_for, make_response
from flask.views import MethodView
from datetime import datetime
from app import db
from app.models.home import string, stringSchema, integer, integerSchema
from flask_jwt_extended import jwt_required, unset_jwt_cookies, get_jwt_identity

home = Blueprint('home', __name__)


@home.route('/')
@jwt_required()
def index():
    name = get_jwt_identity()
    return render_template('home.html', name=name)


@home.route('/logout')
def logout():
    resp = make_response(redirect(url_for('login.index')))
    unset_jwt_cookies(resp)
    return resp


class HomeController(MethodView):
    def post(self):
        json_data = request.get_json()
        input = json_data['input']
        select = json_data['select']
        if select == 'string':
            postDb = string(input=input)
        elif select == "integer":
            postDb = integer(input=input)
        db.session.add(postDb)
        db.session.commit()
        return jsonify(input)

    def get(self):
        dbString = string.query.all()
        schString = stringSchema(many=True)
        outString = schString.dump(dbString)
        dbInteger = integer.query.all()
        schInteger = integerSchema(many=True)
        outInteger = schInteger.dump(dbInteger)
        return jsonify({'Kelas A': outString}, {'Kelas B': outInteger})


home_view = HomeController.as_view('home_view')
home.add_url_rule('/post', view_func=home_view, methods=['POST'])
home.add_url_rule('/get', view_func=home_view, methods=['GET'])
