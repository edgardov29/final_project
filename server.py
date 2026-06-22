from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, request

app = Flask(__name__)

@app.route("/emotionDetector")
def detectar_emocion():
    frase = request.args.get("text")
    result = emotion_detector(frase)
    response = f"For the given statement, the system response is {result}. The dominant emotion is {result['dominant_emotion']}"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
