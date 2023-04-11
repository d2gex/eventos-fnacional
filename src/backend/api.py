from flask import Blueprint, jsonify, request
from flask_cors import CORS

api = Blueprint('api', __name__, url_prefix='/api')
cors = CORS(api, resources={r'/api/*': {"origins": "http://localhost:8080"}})


@api.route('/save_torero_details', methods=['POST'])
def save_torero_details():
    data = request.get_json()
    print(data)
    return jsonify(data)


@api.route('get_torero_details', methods=['GET'])
def get_torero_details():
    return {
        'key': 'value'
    }