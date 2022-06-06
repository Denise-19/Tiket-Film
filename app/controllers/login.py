from flask import render_template, request, Blueprint, jsonify
from flask.views import MethodView
from app.models.user import User
from app import assign_access_refresh_tokens

login = Blueprint('login', __name__)


@login.route('/')
def index():
    return render_template('login.html')


class loginController(MethodView):
    def post(self):
        json_data = request.get_json()
        user = json_data['user']
        password = json_data['password']

        user = User.query.filter_by(username=user).first()

        if not user or not user.checkPassword(password):
            resp = jsonify({'login': False})
            return resp
        return assign_access_refresh_tokens(user.username)


login_view = loginController.as_view('login_view')
login.add_url_rule('/post', view_func=login_view, methods=['POST'])
