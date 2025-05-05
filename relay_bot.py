import requests

# 🔐 Tu token de bot (lo tienes)
token = '8075448930:AAF9TIfe5SklIvKLnDG4ubcj6Aj86Fh4WAo'

# 🧑‍💼 Tu chat ID (lo tienes)
chat_id = '757251632'

# 📝 Tu mensaje RA 1116
mensaje = """
🔔 SETUP ACTIVO – RA 1116

📍 Par: XAU/USD (Sesión Londres)
🎯 Entrada SELL: 3332.40
🔐 SL: 3335.60
🎯 TP1: 3308.10 | 🎯 TP2: 3287.00
📊 RR: 1:3.5 (TP1) / 1:6.8 (TP2)

✅ Confirmación institucional:
• Spike 3334 barrido
• Rechazo M5 confirmado con absorción
• BOS bajista M1 + volumen

🕐 Killzone Londres activa: 07:15 – 10:30 UTC
"""

# Envío del mensaje
url = f'https://api.telegram.org/bot{token}/sendMessage'
params = {'chat_id': chat_id, 'text': mensaje}

r = requests.post(url, params=params)

# Ver resultado
if r.status_code == 200:
    print("✅ Mensaje enviado correctamente.")
else:
    print("❌ Error:", r.text)
