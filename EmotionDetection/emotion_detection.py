import json
import requests


def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = json_input, headers = headers)
    response_text = json.loads(response.text)

    if response.status_code == 200:
        response_text = response_text['emotionPredictions'][0]['emotion']
        dominant = max(response_text, key=response_text.get)
        response_text['dominant_emotion'] = dominant
        return response_text
    else:
        response_text = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
            }
        return response_text
