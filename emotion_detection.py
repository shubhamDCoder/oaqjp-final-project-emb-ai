import requests
import json
def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    body = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url,json = body, headers = header)
    formatted_resposne = json(response.text)
    emotion_prediction = formatted_resposne["emotionPredictions"]
    anger_score = emotion_prediction["anger"]
    disgust_score = emotion_prediction["disgust"]
    fear_score = emotion_prediction["fear"]
    joy_score = emotion_prediction["joy"]
    sadness_score = emotion_prediction["sadness"]
    dominant_emotion
    { 
'anger': anger_score,
'disgust': disgust_score,
'fear': fear_score,
'joy': joy_score,
'sadness': sadness_score,
'dominant_emotion': '<name of the dominant emotion>'
}
