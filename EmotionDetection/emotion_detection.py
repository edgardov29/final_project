import requests
import json

url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    input_json = { "raw_document": { "text": text_to_analyze } } # Construir el JSON de entrada

    response = requests.post(url, headers=headers, json=input_json) # Hacer la petición al servicio Watson

    if response.status_code == 400: # Manejo de error si el servidor devuelve status_code = 400
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    result = response.json() # Procesar la respuesta normal
    emotions = result["emotionPredictions"][0]["emotion"]

    # Calcular emoción dominante
    dominant_emotion = max(emotions, key=emotions.get)
    emotions["dominant_emotion"] = dominant_emotion

    return emotions
