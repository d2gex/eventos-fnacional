import pandas as pd
import simplejson as json
from flask import Blueprint, jsonify, request
from flask_cors import CORS
from src.config import Config
from src.db import models
from src.db.utils import session_scope
from sqlalchemy.exc import IntegrityError

api = Blueprint("api", __name__, url_prefix="/api")
cors = CORS(api, resources={r"/api/*": {"origins": "http://localhost:8080"}})


@api.route("/get_tipo_toreros", methods=["GET"])
def get_tipo_toreros():
    with session_scope() as dbs:
        db_data = dbs.query(models.ModelTipoTorero).all()
        data = [x.to_dict() for x in db_data]
    return jsonify(data)


@api.route("/get_tipo_festejos", methods=["GET"])
def get_tipo_festejos():
    with session_scope() as dbs:
        db_data = dbs.query(models.ModelTipoFestejo).all()
        data = [x.to_dict() for x in db_data]
    return jsonify(data)


@api.route("/get_provincias", methods=["GET"])
def get_provincias():
    with session_scope() as dbs:
        db_data = dbs.query(models.ModelProvincia).all()
        data = [x.to_dict() for x in db_data]
    return jsonify(data)


@api.route("/get_toreros", methods=["GET"])
def get_toreros():
    with session_scope() as dbs:
        db_data = dbs.query(
            models.ModelTorero.nombre_profesional, models.ModelTorero.id
        ).all()
        data = [{"nombre_profesional": row[0], "id": row[1]} for row in db_data]
    return jsonify(data)


@api.route("/get_ganaderias", methods=["GET"])
def get_ganaderias():
    with session_scope() as dbs:
        db_data = dbs.query(models.ModelGanaderia).all()
        data = [x.to_dict() for x in db_data]
    return jsonify(data)


@api.route("/get_old_db_all_records", methods=["GET"])
def get_old_db_all_records():
    df = pd.read_csv(Config.NEW_CSV_DB_PATH)
    records = df.to_dict(orient="records")
    return json.dumps({"data": records}, ignore_nan=True)


@api.route("/save_torero_details", methods=["POST"])
def save_torero_details():
    data = request.get_json()
    record = None
    try:
        for torero_details in data["toreroRow"]:
            record = torero_details
            record[
                "nombre_profesional"
            ] = f"{record['nombre']} {record['apellidos']} {record['apodo']}".strip()
            with session_scope() as s_db:
                s_db.add(models.ModelTorero(**record))
    except IntegrityError:
        data = {
            "status": 0,
            "message": f"Torero '{record['nombre_profesional']}' already exists",
        }
    else:
        data = {"status": 1}

    return jsonify(data)


@api.route("/save_ganaderia_details", methods=["POST"])
def save_ganaderia_details():
    data = request.get_json()
    record = None
    try:
        for ganaderia_details in data["ganaderiaRow"]:
            record = ganaderia_details
            with session_scope() as s_db:
                s_db.add(models.ModelGanaderia(**record))
    except IntegrityError:
        data = {
            "status": 0,
            "message": f"Ganaderia '{record['nombre_ganaderia']}' already exists",
        }
    else:
        data = {"status": 1}

    return jsonify(data)
