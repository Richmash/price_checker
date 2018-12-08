from flask import Blueprint, render_template, request, session, make_response

__author__ = 'richmash'


user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login_user():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if User.is_login_valid(email, password):
            session['email'] = email
            return redirect(url_for(".user_alerts"))

    return render_template("users/login.html") # send user error if their login is invalid


@user_blueprint.route('/register')
def register_user():
    pass

@user_blueprint.route('/alerts')
def user_alert():
    return "This is the alerts page!"

@user_blueprint.route('/logout')
def logout_user():
    pass

@user_blueprint.route('/check_alerts/<string:user_id>')
def check_user_alerts(user_id):
    pass