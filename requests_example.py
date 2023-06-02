# Este script en Python ejemplifica como desde el lenguaje Python se pueden
# enviar peticiones a nuestra aplicacion
import requests

URL = "http://localhost:5000/todo"
ID = "1"

# Envio peticion 'POST'
response = requests.post(URL, json={ "content": "escribir libro" })
print(f"Respuesta a post {response}")

# Envio peticion 'PUT'
response = requests.put(URL + f"/{ID}", json={ "content": "escribir libro sobre la web" })
print(f"Respuesta a put {response}")

# Envio peticion 'DELETE'
response = requests.delete(URL + f"/{ID}")
print(f"Respuesta a delete {response}")
