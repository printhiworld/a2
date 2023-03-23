from flask_restx import Resource, Namespace
from flask import request
from setup_db import db
from config import get_hash

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        data = request.json
        username = data.get('username', None)
        password = data.get('password', None)
        if None in [username, password]:
            return '', 400
        tokens = get_hash()
        return tokens, 201


    def put(self):
        data = request.json
        token = data.get('refresh_token')

        return token, 201

