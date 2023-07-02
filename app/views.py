from datetime import datetime

from flask import render_template, g, url_for, redirect, request
from flask_login import login_user, current_user, logout_user

from app import db, app, login_manager
from app.forms import PostForm
from app.forms import LoginForm, RegisterForm
from app.models import User
from app.models import Post


@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if g.user is None and not g.user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('user/register.html', title='Register', form=form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if request.method == 'POST':
        username = form.user.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('index'))
        return render_template('login.html', error='Invalid username or password')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('index'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/create-post/', methods=['GET', 'POST'])
def create_post():
    if g.user is None or not g.user.is_authenticated:
        return redirect(url_for('index'))
    form = PostForm()
    if request.method == 'POST':
        post = Post(
            title=form.title.data,
            body=form.body.data,
            timestamp=datetime.utcnow(),
            author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_post.html', title='Create Post', form=form)
