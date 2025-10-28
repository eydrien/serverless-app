from flask import jsonify
from google.cloud import storage
import functions_framework

BUCKET_NAME = "qrapp-adriandavid-2025"

@functions_framework.http
def app(request):

    # Manejo preflight CORS
    if request.method == 'OPTIONS':
        response = jsonify({'ok': True})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response, 200

    try:
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blobs = bucket.list_blobs()

        urls = [blob.public_url for blob in blobs]

        response = jsonify({'success': True, 'qrs': urls})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200

    except Exception as e:
        response = jsonify({'success': False, 'error': str(e)})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 500
