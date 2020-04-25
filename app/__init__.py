from flask import Flask, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_restx import Api
from flask_session import Session

db = SQLAlchemy()
cors = CORS()

def create_app(env=None):
    from app.config import config_by_name
    from app.routes import register_routes

    app = Flask(__name__)
    app.config.from_object(config_by_name[env or "dev"])
    api = Api(app, title="")

    register_routes(api, app)

    db.init_app(app)
    cors.init_app(app)

    Session(app)


    @app.route("/health")
    def healthCheck():
        return jsonify('healthy')

    return app