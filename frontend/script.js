const API_URL = "https://us-central1-serverless-qrapp.cloudfunctions.net/generate-qr"; 

document.getElementById("generate-btn").addEventListener("click", async () => {
  const text = document.getElementById("qr-text").value;
  if (!text) {
    alert("Por favor ingresa un texto o URL.");
    return;
  }

  const resultDiv = document.getElementById("result");
  resultDiv.innerHTML = "Generando QR...";

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const data = await res.json();
    if (data.success) {
      resultDiv.innerHTML = `<img src="${data.qr_image}" alt="QR Code">`;
    } else {
      resultDiv.textContent = "Error: " + data.error;
    }
  } catch (err) {
    resultDiv.textContent = "Error en la conexión con el servidor.";
  }
});
