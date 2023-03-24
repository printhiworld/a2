from flask_restx import Resource, Namespace
from flask import request
from models.user import User, UserSchema
from setup_db import db
from decorator import auth_required

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        rs = db.session.query(User).all()
        res = UserSchema(many=True).dump(rs)
        return res, 200


    def post(self, data):
        def create1(self, data):
            obj = User(**data)
            self.session.add(obj)
            self.session.commit()


        '''def create2(self, data):
            return self.create1(data)
'''
        obj = create1(request.json)
        return UserSchema().dump(obj), 201, {'location': f'/users/{obj.id}'}





@user_ns.route('/<int:pk>')
class UserView(Resource):
    @auth_required
    def get(self, pk):
        r = db.session.query(User).get(pk)
        sm_d = UserSchema().dump(r)
        return sm_d, 200

    @auth_required
    def put(self, pk):
        user = db.session.query(User).get(pk)
        req_json = request.json
        user.username = req_json.get("username")
        user.password = req_json.get("password")
        user.role = req_json.get("role")
        db.session.add(user)
        db.session.commit()
        return "", 204

    @auth_required
    def delete(self, pk):
        user = db.session.query(User).get(pk)
        db.session.delete(user)
        db.session.commit()
        return "", 204
