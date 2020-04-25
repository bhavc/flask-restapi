from app import session, config
from flask import request
from flask_restx import Namespace, Resource

from .service import AuthService

api = Namespace('Auth', description="Authorization namespace")

@api.route('/Login')
@api.response(404, 'Could not login user')
class LoginResource(Resource):
    def post(self):
        try:
            return 'Logged in', 200
        except Exception as error:
            return 'Error logging in user', 500


@api.route('/Register')
@api.response(404, 'Could not register user')
class RegisterResource(Resource):
    def post(self):
        try:
           return 'Registered'
        except Exception as error:
            return 'Error registering user', 500