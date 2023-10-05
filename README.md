# API de Reconocimiento de Entidades Nombradas (NER) con Flask y Spacy

## Descripción

Esta API permite identificar entidades nombradas en oraciones en español utilizando Flask y Spacy.

## Instalación

1. Clona este repositorio.
2. Instala las dependencias:

```bash
pip install flask spacy requests
python -m spacy download es_core_news_sm
```

## Uso

### Ejecutar la API

1. Navega hasta el directorio donde se encuentra el archivo de la API.
2. Ejecuta el archivo:

```bash
python api_rest_nlp_ner.py
```

El servicio se iniciará en `http://127.0.0.1:5000/ner`.

### Probar la API con el ejemplo

1. Asegúrate de que la API esté en funcionamiento.
2. Navega hasta el directorio donde se encuentra el script de prueba.
3. Ejecuta el script de prueba:

```bash
python request_example.py
```

La petición enviará las siguientes oraciones como ejemplo:

```
"Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
"San Francisco considera prohibir los robots de entrega en la acera."
```

La respuesta esperada de la API será similar a:

```json
{
 "resultado": [
 {
   "oración": "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
   "entidades": {
     "Apple": "ORG",
     "Reino Unido": "LOC"
   }
 },
 {
   "oración": "San Francisco considera prohibir los robots de entrega en la acera.",
   "entidades": {
     "San Francisco": "LOC"
   }
 }
 ]
}
```

El resultado se imprimirá en la consola.
