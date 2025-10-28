import base64
from flask import request, jsonify
from google.cloud import storage
import functions_framework

BUCKET_NAME = "qrapp-adriandavid-2025"

@functions_framework.http
def app(request):

    # Manejar preflight (CORS)
    if request.method == 'OPTIONS':
        response = jsonify({'ok': True})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response, 200

    try:
        data = request.get_json(silent=True)
        image_data = data.get('image', '')

        if not image_data:
            response = jsonify({'success': False, 'error': 'Imagen no recibida'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response, 400

        image_bytes = base64.b64decode(image_data.split(',')[1])

        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)

        from uuid import uuid4
        file_name = f"qr_{uuid4().hex}.png"

        blob = bucket.blob(file_name)
        blob.upload_from_string(image_bytes, content_type="image/png")
        blob.make_public()

        response = jsonify({
            'success': True,
            'url': blob.public_url
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 200

    except Exception as e:
        response = jsonify({'success': False, 'error': str(e)})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response, 500
