from flask import Blueprint, request, Response
from models.AdminModel import login_handler
import json
import datetime

admin_blueprint = Blueprint("admin", __name__)


@admin_blueprint.route('/login', methods=["POST"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")

    try:
        result = login_handler(email, password)
        resp = Response(
            json.dumps(
                result[1]),
            status=200,
            mimetype="application/json")
        resp.set_cookie(
            key="auth_token",
            value=result[0],
            expires=datetime.datetime.utcnow() + datetime.timedelta(hours=2),
            httponly=True,
            samesite="Strict",
            secure=True)
        return resp
    except Exception as e:
        return Response(
            json.dumps(
                {"error": e.message}),
            status=e.status_code,
            mimetype="application/json")
    except:  # noqa E722
        return Response(json.dumps({"error": "An unexpected error occurred. Please report this issue if this continues."}), status=500, mimetype="application/json")  # noqa E501