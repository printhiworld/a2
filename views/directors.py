from flask_restx import Resource, Namespace
from flask import request
from decorator import auth_required, admin_required
from models.director import Director, DirectorSchema
from setup_db import db

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @admin_required
    def get(self):
            rs = db.session.query(Director).all()
            res = DirectorSchema(many=True).dump(rs)
            return res, 200

    @admin_required
    def post(self, data):
        def create1(self, data):
            obj = Director(**data)
            self.session.add(obj)
            self.session.commit()

        obj = create1(request.json)
        return DirectorSchema().dump(obj), 201, {'location': f'/users/{obj.id}'}

@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        r = db.session.query(Director).get(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, pk):
        director = db.session.query(Director).get(pk)
        req_json = request.json
        director.name = req_json.get("name")
        db.session.add(director)
        db.session.commit()
        return "", 204

    @admin_required
    def delete(self, pk):
        director = db.session.query(Director).get(pk)
        db.session.delete(director)
        db.session.commit()
        return "", 204