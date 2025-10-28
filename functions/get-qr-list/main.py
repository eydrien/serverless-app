from flask import Flask, jsonify
from flask_cors import CORS
from google.cloud import storage

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def list_qrs():
    try:
        client = storage.Client()
        bucket = client.bucket('tu-bucket-name')  # Cambia esto
        blobs = bucket.list_blobs()

        urls = [blob.public_url for blob in blobs]
        return jsonify({'success': True, 'qrs': urls})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
