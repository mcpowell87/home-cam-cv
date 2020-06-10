#!flask/bin/python
from flask import jsonify
from api import api

@api.route('/api/test', methods=['GET'])
def test_get():
    return jsonify({'message': "Hello, world!"})