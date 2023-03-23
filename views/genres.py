from flask_restx import Resource, Namespace
from flask import request
from models.genre import Genre, GenreSchema
from setup_db import db
from decorator import auth_required

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        rs = db.session.query(Genre).all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @auth_required

    def post(self):
        obj = db.session.add(request.json)
        return GenreSchema().dump(obj), 201, {'location': f'/genres/{obj.id}'}

@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        r = db.session.query(Genre).get(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @auth_required
    def put(self, pk):
        genre = db.session.query(Genre).get(pk)
        req_json = request.json
        genre.name = req_json.get("name")
        db.session.add(genre)
        db.session.commit()
        return "", 204

    @auth_required
    def delete(self, pk):
        genre = db.session.query(Genre).get(pk)
        db.session.delete(genre)
        db.session.commit()
        return "", 204