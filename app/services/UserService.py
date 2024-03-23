import app.repos.UserRepo as userRepo


def get_all_users():
    users = list(user.to_dict() for user in userRepo.get_all_users())
    return users


def get_user_by_id(user_id):
    user = userRepo.get_user_by_id(user_id)
    return user.to_dict() if user else None


def add_user(username, email_address, password):
    return userRepo.add_user(username, email_address, password)


def delete_user_by_name(username):
    return userRepo.delete_user_by_name(username)


def delete_user_by_id(user_id):
    return userRepo.delete_user_by_id(user_id)


def delele_all_users():
    return userRepo.delele_all_users()


def get_user_ny_name(username):
    user = userRepo.get_user_ny_name(username)
    return user.to_dict() if user else None


def get_user_by_name_and_email(username, email):
    user = userRepo.get_user_by_name_and_email(username, email)
    return user.to_dict() if user else None
