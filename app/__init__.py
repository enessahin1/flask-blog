from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('app.configuration.DevelopmentConfig')

bs = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.user.views import user_bp
from app.post.views import post_bp

app.register_blueprint(user_bp, url_prefix='')
app.register_blueprint(post_bp, url_prefix='')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    from app.user.models import User
    return User.query.get(int(id))
