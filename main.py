from flask import Flask
from routes.matrix.action import action

def create_app():
    app = Flask(__name__)
    app.register_blueprint(action)

    return app