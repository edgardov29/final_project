from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Página principal con formulario HTML"""
    return render_template("index.html")

@app.route("/emotionDetector")
def detectar_emocion():
    """Endpoint que recibe texto y devuelve emociones"""
    frase = request.args.get("textToAnalyze")
    result = emotion_detector(frase)

    if result["dominant_emotion"] is None:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!", 400

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
