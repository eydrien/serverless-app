import base64
from flask import request, jsonify
from google.cloud import storage
import functions_framework

BUCKET_NAME = "qrapp-adriandavid-2025"

@functions_framework.http
def app(request):
    try:
        data = request.get_json(silent=True)
        image_data = data.get('image', '')

        if not image_data:
            return jsonify({'success': False, 'error': 'Imagen no recibida'}), 400

        # Convertir Base64 → bytes
        image_bytes = base64.b64decode(image_data.split(',')[1])

        # Cliente de Cloud Storage
        client = storage.Client()
        bucket = client.bucket(BUCKET_NAME)

        # Nombre único del archivo
        from uuid import uuid4
        file_name = f"qr_{uuid4().hex}.png"

        blob = bucket.blob(file_name)
        blob.upload_from_string(image_bytes, content_type="image/png")
        blob.make_public()

        return jsonify({
            'success': True,
            'url': blob.public_url
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
