from db.Schema import Admin
from sqlalchemy import exc
from middleware.Authentication import generate_auth_token
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def login_handler(email, password):
    try:
        admin: Admin = Admin.query.filter_by(email=email).first()

        if admin is None or not bcrypt.check_password_hash(admin.hash, password):  # noqa E501
            raise Exception("Invalid email or password", 401)

        admin_data = admin.as_dict()
        auth_token = generate_auth_token(admin_data, "ADMIN_JWT_SECRET_KEY")
        return (auth_token, admin_data)
    except exc.SQLAlchemyError:
        raise Exception("Failed to check login credentials. Try again.", 500)
    except Exception as e:
        if type(e) is not Exception:
            raise Exception("Something went wrong. Please contact our team if this continues.", 500)  # noqa E501
        else:
            raise e
