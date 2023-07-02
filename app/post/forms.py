from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import InputRequired


class PostForm(FlaskForm):
    title = TextAreaField(u'title', validators=[InputRequired()])
    body = TextAreaField(u'body', validators=[InputRequired()])
