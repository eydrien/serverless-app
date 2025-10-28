const GENERATE_URL = "https://generate-qr-q3wzpsnx4q-uc.a.run.app";
const SAVE_URL = "https://save-qr-q3wzpsnx4q-uc.a.run.app";
const LIST_URL = "https://get-qr-list-q3wzpsnx4q-uc.a.run.app";

let lastQR = null;

async function generateQR() {
  const text = document.getElementById('qrText').value.trim();
  if(!text){
    alert("⚠️ Debes ingresar un texto para generar el QR.");
    return;
  }

  try {
    const res = await fetch(GENERATE_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });
    const json = await res.json();
    if(json.success){
      lastQR = json.qr_image;
      document.getElementById('qrResult').innerHTML = `<img src="${json.qr_image}" class="mx-auto mt-4 w-56 h-56 rounded shadow-lg" />`;
    } else {
      alert("❌ Error: " + json.error);
    }
  } catch(e){
    alert("❌ Error en la conexión con el servidor");
  }
}

async function saveQR(){
  if(!lastQR) return alert("⚠️ Primero genera un QR!");
  await fetch(SAVE_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ image: lastQR })
  });
  alert("✅ QR Guardado en la nube!");
}

function downloadQR(url){
  const a = document.createElement('a');
  a.href = url;
  a.download = "qr.png";
  a.click();
}

async function loadHistory(){
  const res = await fetch(LIST_URL);
  const json = await res.json();
  if(json.success){
    const container = document.getElementById('history');
    container.innerHTML = json.qrs.map(url => `
      <div class="bg-gray-800 p-3 rounded-lg shadow text-center">
        <img src="${url}" class="mx-auto rounded mb-2 h-32 w-32 object-contain" />
        <button onclick="downloadQR('${url}')" class="bg-blue-600 hover:bg-blue-700 text-white px-3 py-1 rounded">Descargar</button>
      </div>
    `).join('');
  }
}
