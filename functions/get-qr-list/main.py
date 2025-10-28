from flask import jsonify
from google.cloud import storage
import functions_framework

BUCKET_NAME = "qrapp-adriandavid-2025"

@functions_framework.http
def app(request):
    try:
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)
        blobs = bucket.list_blobs()

        urls = [blob.public_url for blob in blobs]

        return jsonify({
            'success': True,
            'qrs': urls
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
