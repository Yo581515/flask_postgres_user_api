from app.extensions import app
from app.services import UserService as user_service


@app.route('/')
def home():  # put application's code here
    # return 'Hello World!'
    return user_service.get_all_users()


@app.route('/users')
def get_all_users():
    return user_service.get_all_users()


@app.route('/users/id/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    print("route get_user_by_id", user_id)
    return user_service.get_user_by_id(user_id)


@app.route('/users/name/<username>', methods=['GET'])
def get_user_ny_name(username):
    return user_service.get_user_ny_name(username)


@app.route('/users/name/<username>', methods=['POST'])
def delete_user_by_name(username):
    return user_service.delete_user_by_name(username)


@app.route('/users', methods=['POST'])
def add_user(name, email, password):
    return user_service.add_user(name, email, password)
