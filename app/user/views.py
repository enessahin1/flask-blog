from flask import redirect, url_for, render_template, request, Blueprint
from flask_login import login_user, current_user, logout_user

from app import db
from app.user.forms import LoginForm, RegisterForm
from app.user.models import User

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user is None and not current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('user/register.html', title='Register', form=form)


@user_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('post_bp.index'))
    form = LoginForm()
    if request.method == 'POST':
        username = form.user.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('post_bp.index'))
        return render_template('login.html', error='Invalid username or password')
    return render_template('login.html', title='Login', form=form)


@user_bp.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('post_bp.index'))
