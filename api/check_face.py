import os
import uuid

from api import api
from flask import jsonify, request, abort
from werkzeug.utils import secure_filename

if not os.path.exists("C:\\Uploads"):
    os.makedirs("C:\\Uploads")

@api.route('/api/check_face', methods=['POST'])
def check_face():
    if not request.form['webhook'] or not request.form['payload']:
        abort(400, "Missing required parameters.")
    
    if "file" not in request.files:
        abort(400, "No file part")
    
    file = request.files["file"]

    if file.filename == '':
        abort(400, "Missing filename")

    filename = secure_filename(file.filename)
    
    # upload file to analyze
    try:
        file.save(os.path.join("C:\\Uploads", str(uuid.uuid4()) + "-" + filename))
    except Exception as e:
        abort(500, jsonify({'error': "File upload failed.", 'exception': str(e)}))
    
    # ToDo: Request facial recognition

    return jsonify({'message': "Success"}), 201