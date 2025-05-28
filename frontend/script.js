const API_BASE = 'http://localhost:5000/api';

document.getElementById('sendBtn').addEventListener('click', async () => {
  const to = document.getElementById('phone').value;
  const otp = Math.floor(1000 + Math.random()*9000);
  const res = await fetch(`${API_BASE}/send_sms`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ to, otp })
  });
  const data = await res.json();
  document.getElementById('sendResult').innerText =
    res.ok ? `Sent! SID: ${data.sid}` : `Error: ${data.error}`;
});

document.getElementById('predictBtn').addEventListener('click', async () => {
  const text = document.getElementById('smsText').value;
  const res = await fetch(`${API_BASE}/predict`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text })
  });
  const { phishing_score } = await res.json();
  document.getElementById('predictResult').innerText = `Phishing score: ${phishing_score}`;
});
