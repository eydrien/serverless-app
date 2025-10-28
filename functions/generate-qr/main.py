import json
import qrcode
import base64
from io import BytesIO
from flask import jsonify, request
import functions_framework

@functions_framework.http
def app(request):
    try:
        data = request.get_json(silent=True)
        text = data.get('text', '')

        if not text:
            return jsonify({'success': False, 'error': 'Texto vacío'}), 400

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
