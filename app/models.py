from app.extensions import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

    def __repr__(self):
        return f'[User @ {self.username} @ {self.email_address} @ {self.password_hash}]'

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email_address": self.email_address,
            "password_hash": self.password_hash
        }
