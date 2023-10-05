# Importamos las bibliotecas necesarias
from flask import Flask, request, jsonify
import spacy

# Creamos una instancia de Flask y cargamos el modelo de Spacy para español
app = Flask(__name__)
nlp = spacy.load("es_core_news_sm")

@app.route('/ner', methods=['POST'])
def named_entity_recognition():
    try:
        # Obtenemos el JSON del cuerpo de la petición
        data = request.json

        # Verificamos que el JSON contenga el campo 'oraciones'
        if "oraciones" not in data:
            return jsonify({"error": "El campo 'oraciones' no está presente en el JSON enviado."}), 400

        # Extraemos la lista de oraciones del JSON o una lista vacía si no existe
        sentences = data.get('oraciones', [])
        
        results = []

        # Procesamos cada oración con Spacy
        for sentence in sentences:
            doc = nlp(sentence)
            entities = {}

            # Para cada entidad encontrada, guardamos su texto y etiqueta
            for ent in doc.ents:
                entities[ent.text] = ent.label_

            # Agregamos los resultados a la lista de respuestas
            result = {
                "oración": sentence,
                "entidades": entities
            }
            results.append(result)

        # Devolvemos el resultado en formato JSON
        return jsonify({"resultado": results})

    # Captura cualquier error inesperado
    except Exception as e:
        return jsonify({"error": "Ha ocurrido un error al procesar la solicitud: " + str(e)}), 500

# Si este archivo se ejecuta como el principal, iniciamos la aplicación Flask
if __name__ == "__main__":
    app.run(debug=True)
