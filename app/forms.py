from flask_wtf import FlaskForm
from wtforms import TextAreaField, PasswordField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    user = TextAreaField(u'username', validators=[InputRequired()])
    password = PasswordField(u'password', validators=[InputRequired()])


class RegisterForm(FlaskForm):
    username = TextAreaField(u'username', validators=[InputRequired()])
    password = PasswordField(u'password', validators=[InputRequired()])
    repeat_password = PasswordField(u'repeat password', validators=[InputRequired()])


class PostForm(FlaskForm):
    title = TextAreaField(u'title', validators=[InputRequired()])
    body = TextAreaField(u'body', validators=[InputRequired()])
