from flask import render_template, request, jsonify, Blueprint
from flask.views import MethodView
from app import db
from app.models.user import User

register = Blueprint('register', __name__)


@register.route('/')
def index():
    return render_template('register.html')


class registerController(MethodView):
    def post(self):
        json_data = request.get_json()
        user = json_data['user']
        email = json_data['email']
        password = json_data['password']

        hashPass = User().setPassword(password)
        postdb = User(username=user, email=email, password=hashPass)

        db.session.add(postdb)
        db.session.commit()

        return jsonify(user, email, hashPass)


register_view = registerController.as_view('register_view')
register.add_url_rule('/post', view_func=register_view, methods=['POST'])
