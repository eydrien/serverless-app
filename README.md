
# Generador de Códigos QR Serverless

Este proyecto implementa un generador de códigos QR usando funciones serverless en Google Cloud Functions, almacenamiento en Google Cloud Storage y un frontend estático.

## 🌐 URLs del Proyecto

- **Frontend:** https://storage.googleapis.com/qrapp-frontend-2025/index.html
- **Generar QR:** https://generate-qr-q3wzpsnx4q-uc.a.run.app
- **Guardar QR:** https://save-qr-q3wzpsnx4q-uc.a.run.app
- **Listar Historial:** https://get-qr-list-q3wzpsnx4q-uc.a.run.app

## ⚙️ Arquitectura
1. El usuario genera un código QR desde el frontend.
2. La función **generate-qr** crea el QR y lo devuelve como imagen base64.
3. La función **save-qr** almacena el QR en un bucket de Cloud Storage.
4. La función **get-qr-list** devuelve la lista de imágenes guardadas.
5. El frontend muestra el historial y permite descargar cada QR.

## 🚀 Despliegue del Frontend
```bash
gsutil web set -m index.html gs://qrapp-frontend-2025
gsutil cp index.html script.js gs://qrapp-frontend-2025
gsutil iam ch allUsers:objectViewer gs://qrapp-frontend-2025
```

## 🧾 Dependencias Backend (requirements.txt)
```
flask
flask-cors
qrcode
Pillow
google-cloud-storage
functions-framework
```

## 🛠 Errores y Solución

### 1) ❌ CORS bloqueando solicitudes desde el frontend
**Causa:** La función no tenía headers CORS  
**Solución:** Agregar:
```python
from flask_cors import CORS
CORS(app)
```

### 2) ❌ Error: `No module named 'PIL'`
**Solución:** Agregar `Pillow` a `requirements.txt`.

### 3) ❌ La función no arranca en Cloud Run (Gen2) - Puerto incorrecto
**Causa:** Flask por defecto usa 5000, Cloud Run usa `$PORT`  
**Solución:**
```python
import os
app.run(port=int(os.environ.get("PORT", 8080)))
```

### 4) ❌ EntryPoint incorrecto
**Solución:** En el deploy:
```
--entry-point app
```

## 📸 Capturas (agrega cuando tengas)
```
[Pantalla Principal]<img width="1013" height="299" alt="image" src="https://github.com/user-attachments/assets/5988ad20-af38-4cea-95c8-ac6b43942ec5" />
[QR Generado]<img width="715" height="337" alt="image" src="https://github.com/user-attachments/assets/c9bfad1d-5748-48e4-bc73-dc01751e3c8a" />
[Historial]<img width="643" height="431" alt="image" src="https://github.com/user-attachments/assets/80c3a845-f6ea-44ed-8204-06901413393d" />

```

## 👨‍💻 Autor
Adrian David González Romero
