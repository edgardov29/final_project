from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detectar_emocion():
    # Obtener el texto desde el parámetro GET
    frase = request.args.get("text")

    # Llamar a la función de detección
    result = emotion_detector(frase)

    # Verificar si la emoción dominante es None
    if result["dominant_emotion"] is None:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!", 400

    # Respuesta normal en formato JSON
    response = {
        "text": frase,
        "anger": result["anger"],
        "disgust": result["disgust"],
        "fear": result["fear"],
        "joy": result["joy"],
        "sadness": result["sadness"],
        "dominant_emotion": result["dominant_emotion"]
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
