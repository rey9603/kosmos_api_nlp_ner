# Importamos las bibliotecas necesarias(request para hacer peticiones a la api y json para codificar y decodificar datos en formato JSON )
import requests
import json

# URL de la API Flask en localhost
url = "http://127.0.0.1:5000/ner"
# Definimos los encabezados de la petición
headers = {
    "Content-Type": "application/json"
}
# Definimos el cuerpo de la petición con las oraciones de ejemplo
data = {
    "oraciones": [
        "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera."
    ]
}

# Realizamos la petición POST a nuestra API
response = requests.post(url, headers=headers, data=json.dumps(data))

# Imprimimos el código de respuesta y el contenido de la respuesta
print("Código de respuesta:", response.status_code)
print("Resultado:")


#Cadena JSON resultante formateada con un indentado de 4 espacios y devolución de los carácteres tal y como están.
print(json.dumps(response.json(), indent=4, ensure_ascii=False)) 
