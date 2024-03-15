from sqlalchemy.exc import IntegrityError
from app.extensions import db, app
from app.models import User
from decouple import config


def create_app():
    try:
        POSTGRES_URL = config("POSTGRES_URL")
        POSTGRES_USER = config("POSTGRES_USER")
        POSTGRES_PW = config("POSTGRES_PW")
        POSTGRES_DB = config("POSTGRES_DB")
        print(f"POSTGRES_URL: {POSTGRES_DB}")
        DB_URL = ('postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format
            (
            user=POSTGRES_USER,
            pw=POSTGRES_PW,
            url=POSTGRES_URL,
            db=POSTGRES_DB
        ))
        app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
    except Exception as e:
        print(f"Error when reading credentials: {e}")
    db.init_app(app)

    with app.app_context():
        try:
            db.create_all()
            print("Database created")
        except Exception as e:
            print(f"Error when creating database: {e}")

        print('All tasks in the database:')

        print()

        print("All users in the database:")
        print_all_users()

    # Your database initialization code

    # Import routes after initializing db to avoid circular imports
    from app import routes

    return app





def print_all_users():
    try:
        print(User.query.filter(User.id < 3).all())
    except IntegrityError:
        db.session.rollback()
        print('cant find the task with this id less than 3')


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

