"""File imported by gunicorn which defines the server"""
from flask import Flask

try:
    # Wrap in try to prevent crashing docker image
    from src.app import create_app

    debug = True
    title = "My Slideshow"
    app = create_app(title, debug)
    app.scripts.config.serve_locally = debug
    server = app.server

except Exception as error:
    print(error, flush=True)
    server = Flask(__name__)

if __name__ == "__main__":
    from src.app import create_app

    app = create_app(title, debug)
    app.run_server(debug=True, port="8000", host="0.0.0.0")
