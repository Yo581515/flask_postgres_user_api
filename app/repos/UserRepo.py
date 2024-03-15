from sqlalchemy.exc import IntegrityError

from app import db, User


def add_user(username, email_address, password):
    new_user = User(username=username, email_address=email_address, password_hash=password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        return False


def get_all_users():
    try:
        return User.query.all()
    except IntegrityError:
        db.session.rollback()
        return False


def get_user_by_id(user_id):
    try:
        return User.query.get(user_id)
    except IntegrityError:
        db.session.rollback()
        return False


def delete_user(user):
    try:
        db.session.delete(user)
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        return False


def delete_user_by_name(username):
    try:
        user = User.query.filter_by(username=username).first()
        db.session.delete(user)
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        return False


def delele_all_users():
    try:
        User.query.delete()
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False


def get_user_ny_name(username):
    try:
        return User.query.filter_by(username=username).first()
    except IntegrityError:
        db.session.rollback()
        return False


def get_user_by_name_and_email(username, email):
    try:
        return User.query.filter_by(username=username, email_address=email).first()
    except IntegrityError:
        db.session.rollback()
        return False


def delete_user_by_id(user_id):
    try:
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return True
    except IntegrityError:
        db.session.rollback()
        return False
