from datetime import datetime

from flask import redirect, url_for, g, request, render_template, Blueprint
from flask_login import current_user

from app import db
from app.post.forms import PostForm
from app.post.models import Post

post_bp = Blueprint('post_bp', __name__)


@post_bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@post_bp.route('/create-post/', methods=['GET', 'POST'])
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
