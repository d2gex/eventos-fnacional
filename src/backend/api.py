import pandas as pd
import simplejson as json
from flask import Blueprint, jsonify, request
from flask_cors import CORS
from src.config import Config
from src.db import models, api_db
from src.backend import db_to_datatable

api = Blueprint("api", __name__, url_prefix="/api")
cors = CORS(api, resources={r"/api/*": {"origins": "http://localhost:8080"}})


@api.route("/get_tipo_toreros", methods=["GET"])
def get_tipo_toreros():
    return jsonify(api_db.ApiDB.get_table(models.ModelTipoTorero))


@api.route("/get_tipo_festejos", methods=["GET"])
def get_tipo_festejos():
    return jsonify(api_db.ApiDB.get_table(models.ModelTipoFestejo))


@api.route("/get_provincias", methods=["GET"])
def get_provincias():
    return jsonify(api_db.ApiDB.get_table(models.ModelProvincia))


@api.route("/get_tipo_premios", methods=["GET"])
def get_tipo_premios():
    return jsonify(api_db.ApiDB.get_table(models.ModelTipoPremio))


@api.route("/get_poblaciones", methods=["GET"])
def get_poblaciones():
    return jsonify(api_db.ApiDB.get_table(models.ModelPoblacion))


@api.route("/get_ganaderias", methods=["GET"])
def get_ganaderias():
    return jsonify(api_db.ApiDB.get_table(models.ModelGanaderia))


@api.route("/get_toreros", methods=["GET"])
def get_toreros():
    db_data = api_db.ApiDB.get_toreros()
    return jsonify(db_data)


@api.route("/get_old_db_all_records", methods=["GET"])
def get_old_db_all_records():
    df = pd.read_csv(Config.NEW_CSV_DB_PATH)
    records = df.to_dict(orient="records")
    return json.dumps(records, ignore_nan=True)


@api.route("/get_db_all_records", methods=["GET"])
def get_db_all_records():
    db_result = api_db.ApiDB.get_all_festejos()
    to_datatable = db_to_datatable.DbToDataTable()
    table = to_datatable.run(db_result)
    return jsonify(table)


@api.route("/save_torero_details", methods=["POST"])
def save_torero_details():
    client_data = request.get_json()
    db_result = api_db.ApiDB.save_torero_details(client_data)
    if not db_result:
        data = {"status": 1}
    else:
        data = {
            "status": 0,
            "message": f"Torero '{db_result['nombre_profesional']}' ya existe en la base de datos "
            f"o ha sido provisto por duplicado",
        }
    return jsonify(data)


@api.route("/save_ganaderia_details", methods=["POST"])
def save_ganaderia_details():
    client_data = request.get_json()
    db_result = api_db.ApiDB.save_ganaderia_details(client_data)
    if not db_result:
        data = {"status": 1}
    else:
        data = {
            "status": 0,
            "message": f"Torero '{db_result['nombre_ganaderia']}' ya existe en la base de datos "
            f"o ha sido provisto por duplicado",
        }
    return jsonify(data)


@api.route("/save_festejos", methods=["POST"])
def save_festejos():
    client_data = request.get_json()
    error_details = api_db.ApiDB.save_festejos(client_data)
    if not error_details:
        return jsonify(data={"status": 1})

    if error_details == "toreros":
        message = f"Has introducido toreros duplicados. Múltiples premios se pueden añadir para un único torero"
    else:
        message = f"Hay introducido ganaderías duplicadas."

    return jsonify(
        {
            "status": 0,
            "message": message,
        }
    )
