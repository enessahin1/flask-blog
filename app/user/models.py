from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(500))
    first_name = db.Column(db.String(500))
    last_name = db.Column(db.String(500))
    email = db.Column(db.String(120), unique=True)
    posts = db.relationship('Post', backref='author', lazy=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f'<User {self.username}>'
