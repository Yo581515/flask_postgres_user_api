from app import create_app
from app.services import UserService as user_service

app = create_app()

with app.app_context():
    user_service.delele_all_users()
    # test adding
    test_user1 = user_service.add_user('user1', 'user1@mail.com', '123456')
    test_user2 = user_service.add_user('user2', 'user2@mail.com', '234567')
    test_user3 = user_service.add_user('user3', 'user3@mail.com', '345678')
    # test get_all_users
    print("service get all users")
    users = user_service.get_all_users()
    print(users)
    print()
    print("get user by id")
    delete_id = users[0]['id']
    print(delete_id)
    print(user_service.get_user_by_id(delete_id))
    print()
    print("update user")
    user = user_service.get_user_ny_name("user2")
    print("")
    print("user to be updated")
    print(user_service.get_user_by_id(user['id']))
    print()
    print("delete user")
    user_service.delete_user_by_name(users[-1]['username'])
    print(user_service.get_all_users())
    print()
