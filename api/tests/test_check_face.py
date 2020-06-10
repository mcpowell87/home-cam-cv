import os
import sys
from api import api
from flask import json

def test_test_get_api_call():
    payload = {
        "payload": "test",
        "webhook": "testhook",
        "file": open(os.path.join(sys.path[0], 'api/tests/testImage.png'), 'rb')
    }
    response = api.test_client().post(
        '/api/check_face',
        data = payload
    )

    data = response.get_data(as_text=True)

    print(data)

    assert response.status_code == 201