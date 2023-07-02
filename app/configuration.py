class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///flask_proje_db.sqlite'
    BOOTSTRAP_FONTAWESOME = True
    SECRET_KEY = "NEW_SECRET_KEY"
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(Config):
    DEBUG = True
