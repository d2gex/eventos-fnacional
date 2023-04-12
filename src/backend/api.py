from flask import Blueprint, jsonify, request
from flask_cors import CORS
from src.db import models
from src.db.utils import session_scope

api = Blueprint("api", __name__, url_prefix="/api")
cors = CORS(api, resources={r"/api/*": {"origins": "http://localhost:8080"}})


@api.route("/get_tipo_toreros", methods=["GET"])
def get_tipo_toreros():
    with session_scope() as dbs:
        db_data = dbs.query(models.ModelTipoTorero).all()
        data = [x.to_dict() for x in db_data]
    return jsonify(data)


@api.route("/get_provincias", methods=["GET"])
def get_provincias():
    with session_scope() as dbs:
        db_data = dbs.query(models.ModelProvincia).all()
        data = [x.to_dict() for x in db_data]
    return jsonify(data)


@api.route("/save_torero_details", methods=["POST"])
def save_torero_details():
    data = request.get_json()
    db_data = [
        models.ModelTorero(**torero_details) for torero_details in data["toreroRow"]
    ]
    with session_scope() as s_db:
        s_db.add_all(db_data)
    return jsonify(data)


@api.route("/save_ganaderia_details", methods=["POST"])
def save_ganaderia_details():
    data = request.get_json()
    db_data = [
        models.ModelGanaderia(**ganaderia_details)
        for ganaderia_details in data["ganaderiaRow"]
    ]
    with session_scope() as s_db:
        s_db.add_all(db_data)
    return jsonify(data)


@api.route("get_torero_details", methods=["GET"])
def get_torero_details():
    return {"key": "value"}
