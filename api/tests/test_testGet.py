from api import api
from flask import json

def test_test_get_api_call():
    response = api.test_client().get(
        '/api/test'
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data['message'] == "Hello, world!"