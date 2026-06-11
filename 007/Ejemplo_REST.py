import requests
import json
from datetime import datetime

# Módulo REQUESTS
# Ejemplo utilizando la API de Open Notify http://api.open-notify.org/
# Utiliza la función request.get() para conectarse a una API inexistente
response = requests.get("http://api.open-notify.org/esta-api-no-existe")
print(response.status_code)

print('\n')

# Función request.get() con código de estado 200
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)

print('\n')

# Función response.json() devuelve datos utilizando la API
print(response.json())
print(type(response.json()))

def json_print(objeto):
    texto = json.dumps(objeto, sort_keys=True, indent=4)
    print(texto)
    
json_print(response.json())

print('Datos de la ISS:\n')

# Obtener datos de iss-now.json
respuesta = requests.get("http://api.open-notify.org/iss-now.json")
print(respuesta.status_code)

def json_print(objeto):
    texto = json.dumps(objeto, sort_keys=True, indent=4)
    print(texto)
    
json_print(respuesta.json())

print('Fecha y hora:\n')

# Módulo DATETIME
# Extrae los datos de "timestamp"
# Presenta los datos con formato fecha

fecha_unix = respuesta.json()["timestamp"]
json_print(f'Fecha formato Unix: {fecha_unix}')

fecha = datetime.fromtimestamp(fecha_unix)
json_print(f'Fecha formato normal: {fecha}')