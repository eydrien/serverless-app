from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import storage
import base64, uuid

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def save_qr():
    try:
        data = request.get_json()
        image_data = data.get('image', '')
        if not image_data:
            return jsonify({'success': False, 'error': 'No image data'}), 400

        # Crear cliente de Storage
        client = storage.Client()
        bucket = client.bucket('qrapp-adriandavid-2025')
        blob_name = f"{uuid.uuid4()}.png"

        # Convertir base64 a bytes y guardar
        image_bytes = base64.b64decode(image_data.split(',')[1])
        blob = bucket.blob(blob_name)
        blob.upload_from_string(image_bytes, content_type='image/png')
        blob.make_public()

        return jsonify({'success': True, 'url': blob.public_url})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
