import json
import qrcode
import base64
from io import BytesIO
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def generate_qr():
    try:
        data = request.get_json()
        text = data.get('text', '')
        if not text:
            return jsonify({'success': False, 'error': 'Texto vacío'}), 400

        # Generar el código QR
        qr = qrcode.make(text)
        buffer = BytesIO()
        qr.save(buffer, format='PNG')
        qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        return jsonify({
            'success': True,
            'qr_image': f"data:image/png;base64,{qr_base64}"
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
#para probar de manera local  
if __name__ == '__main__':
    app.run(debug=True, port=5000)
