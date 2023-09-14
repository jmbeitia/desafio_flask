from routes.UserRoute import user_blueprint
from routes.AdminRoute import admin_blueprint
from flask import Blueprint


server_blueprint = Blueprint("server", __name__)
server_blueprint.register_blueprint(user_blueprint, url_prefix="/users")
server_blueprint.register_blueprint(admin_blueprint, url_prefix="/admin")
