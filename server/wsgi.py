import os
from settings import app
from flask import Response


def run_app():
    port = int(os.environ.get('PORT', 8080))
    bind = f"0.0.0.0:{port}"
    cmd = f"gunicorn --bind {bind} wsgi:app"
    os.system(cmd)


@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path):

    return Response("Sitio en proceso de construcción 🚧🏗️👷🏼‍♂️", status=200)


if __name__ == '__main__':
    run_app()
