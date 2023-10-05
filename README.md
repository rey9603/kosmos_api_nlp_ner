# kosmos_api_nlp_ner
Api para realizar NER usando Spacy para Kosmos

API de Reconocimiento de Entidades Nombradas (NER) con Flask y Spacy
Esta API permite identificar entidades nombradas en oraciones en español utilizando Flask y Spacy.

Descripción
API Flask: Un servicio web simple que acepta oraciones en español y devuelve las entidades identificadas junto con sus tipos.

Script de prueba: Un script para realizar peticiones POST a la API y visualizar las respuestas en el formato.

Instalación:
1-Clona este repositorio.
2-Instala las dependencias: pip install flask spacy requests python -m spacy download es_core_news_sm

Uso:
Ejecutar la API
Navega hasta el directorio donde se encuentra el archivo de la API.
Ejecuta el archivo:
python api_rest_nlp_ner.py.py

El servicio se iniciará en http://127.0.0.1:5000/ner
Verás la respuesta de la API en la consola.

Estructura de los Códigos
API Flask:

Se inicia una instancia de Flask y se carga el modelo de Spacy para español.
Se define una ruta /ner que procesa las oraciones enviadas y devuelve las entidades identificadas.
Se incluye manejo de errores básico para asegurar respuestas coherentes.

Script de prueba:
Se utiliza la biblioteca requests para enviar una petición POST a la API.
Se imprime la respuesta de la API en la consola.
