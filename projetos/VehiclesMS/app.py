from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_migrate import Migrate

from extensions import db, ma
from routes.vehicle import register_routes


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/vehicle'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, db)
    register_routes(app)
    docs = FlaskApiSpec(app)
    docs.register_existing_resources()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)

    return app


if __name__ == '__main__':
    create_app().run(debug=True, port=8001)
