from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/save_torero_details', methods=['POST'])
def save_torero_details(data):
    pass


@api.route('get_torero_details', methods=['GET'])
def get_torero_details():
    return {
        'key': 'value'
    }