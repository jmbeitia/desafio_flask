from flask import Blueprint, request, Response, g
from models.UserModel import register_handler, login_handler
import datetime
import json
from middleware.Authentication import authenticate_user

user_blueprint = Blueprint("users", __name__)


@user_blueprint.route("/login", methods=["POST"])
def login():
    email = request.json.get("email")
    password = request.json.get("password")

    try:
        result = login_handler(email, password)
        resp = Response(json.dumps(
           result[1]),
           status=200,
           mimetype="application/json")
        resp.set_cookie(key="auth_token",
                        value=result[0],
                        expires=datetime.datetime.utcnow() + datetime.timedelta(hours=3),  # noqa E501
                        httponly=True, samesite="Strict", secure=True)
        return resp
    except Exception as e:
        return Response(json.dumps(
           {"error": e.message}),
           status=e.status_code,
           mimetype="application/json")
    except:  # noqa E722
        return Response(json.dumps({"error": "An unexpected error occurred. Please report this issue if this continues."}), status=500, mimetype="application/json")  # noqa E501


@user_blueprint.route("/jwt-login", methods=["GET"])
@authenticate_user
def jwt_login():
    token = g.token
    return Response(
        json.dumps(
            token["sub"]),
        status=200,
        mimetype="application/json")


@user_blueprint.route("/register", methods=["POST"])
def register():
    email = request.json.get("email")
    password = request.json.get("password")

    try:
        register_handler(email, password)
        return Response(
            json.dumps(
                {"success": "Account created"}),
            status=201,
            mimetype="application/json")
    except Exception as e:
        return Response(
            json.dumps(
                {"error": e.message}),
            status=e.status_code,
            mimetype="application/json")
    except:  # noqa E722
        return Response(json.dumps({"error": "An unexpected error occurred. Please report this issue if this continues."}), status=500, mimetype="application/json")  # noqa E501


@user_blueprint.route("/logout", methods=["GET"])
@authenticate_user
def logout():
    try:
        resp = Response(
            json.dumps(
                {"success": "Logged out"}),
            status=200,
            mimetype="application/json")
        resp.set_cookie(
            "auth_token",
            "",
            expires=0,
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
