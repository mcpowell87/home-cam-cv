from api import api
from flask import jsonify, make_response

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)