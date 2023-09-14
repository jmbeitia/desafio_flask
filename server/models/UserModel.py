from utils.HashPassword import hash_password
import settings
from db.Schema import User
from sqlalchemy import exc
from middleware.Authentication import generate_auth_token
from flask_bcrypt import Bcrypt

MAX_ITEM_QUANTITY = 10
bcrypt = Bcrypt()


def login_handler(email, password):
    try:
        user: User = User.query.filter_by(email=email).first()

        if user is None or not bcrypt.check_password_hash(user.hash, password):
            raise Exception("Invalid email or password", 401)

        user_data = user.as_dict()
        auth_token = generate_auth_token(user_data, "USER_JWT_SECRET_KEY")

        return (auth_token, user_data)

    except exc.SQLAlchemyError:
        raise Exception("Failed to check login credentials. Try again.", 500)

    except Exception as e:
        if type(e) is not Exception:
            raise Exception(
                "Something went wrong. Please contact our team if this continues.", 500)  # noqa E501
        else:
            raise e


def register_handler(email, password):
    try:
        hash = hash_password(password)
        new_user = User(email=email, hash=hash)
        settings.db.session.add(new_user)
        settings.db.session.commit()

    except exc.SQLAlchemyError:
        raise Exception("Failed to create user account. Try again.", 500)

    except Exception as e:
        if type(e) is not Exception:
            raise Exception("Something went wrong. Please contact our team if this continues.", 500)  # noqa E501
        else:
            raise e
