from flask_restx import Resource, Namespace
from flask import request
from decorator import auth_required
from models.director import Director, DirectorSchema
from setup_db import db

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
            rs = db.session.query(Director).all()
            res = DirectorSchema(many=True).dump(rs)
            return res, 200

    @auth_required

    def post(self):
        obj = db.session.add(request.json)
        return DirectorSchema().dump(obj), 201, {'location': f'/directors/{obj.id}'}


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        r = db.session.query(Director).get(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @auth_required
    def put(self, pk):
        director = db.session.query(Director).get(pk)
        req_json = request.json
        director.name = req_json.get("name")
        db.session.add(director)
        db.session.commit()
        return "", 204

    @auth_required
    def delete(self, pk):
        director = db.session.query(Director).get(pk)
        db.session.delete(director)
        db.session.commit()
        return "", 204