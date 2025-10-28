# 🧩 Generador de Códigos QR Serverless

Este proyecto implementa una **aplicación web serverless** usando
**Google Cloud Functions** como backend y un **frontend ligero** en
HTML, CSS y JavaScript.\
Permite generar códigos QR desde texto o URLs, guardarlos en la nube y
listar los generados.

------------------------------------------------------------------------

## ⚙️ Arquitectura del Sistema

    Frontend (HTML/JS)
        ↓
    API Gateway
        ↓
    Google Cloud Functions (Backend)
        ↓
    Google Cloud Storage (para guardar imágenes)

Las funciones se comunican mediante solicitudes HTTP (POST/GET) y
devuelven respuestas JSON.

------------------------------------------------------------------------

## 🧠 Funciones Implementadas

  -----------------------------------------------------------------------
  Nombre                    Descripción
  ------------------------- ---------------------------------------------
  **generate-qr**           Genera un código QR a partir de texto
                            recibido en JSON.

  **save-qr**               Guarda la imagen QR en Cloud Storage y
                            devuelve su URL pública.

  **get-qr-list**           Lista todas las imágenes QR almacenadas en el
                            bucket.
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 🌐 URLs de Despliegue 
  -------------------------------------------------------------------------------------------------------------------------
  Servicio                                         URL
  ------------------------------------------------ ------------------------------------------------------------------------
  Frontend                                         https://storage.googleapis.com/qrapp-frontend-2025/index.html

  generate-qr                                      https://us-central1-qr-generator-428718.cloudfunctions.net/generate-qr

  save-qr                                          https://us-central1-qr-generator-428718.cloudfunctions.net/save-qr

  get-qr-list                                      https://us-central1-qr-generator-428718.cloudfunctions.net/get-qr-list
  -------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## 🚀 Despliegue en Google Cloud

``` bash
# Autenticación
gcloud auth login

# Configuración del proyecto
gcloud config set project qr-generator-428718

# Despliegue de funciones
gcloud functions deploy generate-qr --runtime python39 --trigger-http --allow-unauthenticated --source ./generate-qr
gcloud functions deploy save-qr --runtime python39 --trigger-http --allow-unauthenticated --source ./save-qr
gcloud functions deploy get-qr-list --runtime python39 --trigger-http --allow-unauthenticated --source ./get-qr-list
```

------------------------------------------------------------------------

## 🧾 Estructura del Proyecto

    serverless-qrapp/
    ├── README.md
    ├── frontend/
    │   ├── index.html
    │   ├── style.css
    │   └── script.js
    ├── functions/
    │   ├── generate-qr/
    │   │   ├── main.py
    │   │   └── requirements.txt
    │   ├── save-qr/
    │   │   ├── main.py
    │   │   └── requirements.txt
    │   ├── get-qr-list/
    │   │   ├── main.py
    │   │   └── requirements.txt
    │   └── deployment.yaml
    └── docs/
        ├── architecture.md
        ├── api-documentation.md
        └── screenshots/

------------------------------------------------------------------------

## 💰 Costos Estimados y Ventajas

**Costo:** \$0 (dentro del Free Tier de Google Cloud).

**Ventajas del modelo Serverless:** - Escalado automático desde 0 hasta
miles de peticiones. - Pago solo por uso. - Sin mantenimiento de
servidores. - Integración directa con otros servicios de Google Cloud.

**Limitaciones:** - Cold starts (primer request puede ser más lento). -
Límite de tiempo de ejecución (5-15 min). - Dependencia del proveedor
(vendor lock-in).

------------------------------------------------------------------------



------------------------------------------------------------------------

📆 **Autor:** Adrian David González Romero\
📅 **Fecha:** Octubre 2025\
📍 **Proyecto académico - Computación en la Nube**
