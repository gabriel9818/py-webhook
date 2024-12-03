import requests
import json

# URL del endpoint del webhook
webhook_url = 'http://127.0.0.1:5000/webhook'

# Datos que se enviarán al servidor
data = {
    'num1': 10,  # Cambia este valor para probar con otros números
    'num2': 20   # Cambia este valor para probar con otros números
}

# Enviar la solicitud POST
response = requests.post(
    webhook_url,
    data=json.dumps(data),
    headers={'Content-Type': 'application/json'}
)

# Mostrar la respuesta del servidor
print("Respuesta del servidor:", response.json())
