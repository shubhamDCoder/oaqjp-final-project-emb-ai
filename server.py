"""This module is to start a  flask based emotion detector app"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_emotions():
    """analyse the emotions"""
    text_to_analyze = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyze)
    anger = res['anger']
    if anger is None:
        return "Invalid text! Please try again!"
    return (f"For the given statement1, the system response is 'anger': {res['anger']},"
    f"'disgust': {res['disgust']}, 'fear': {res['fear']}," 
    f"'joy': {res['joy']} and 'sadness': {res['sadness']}." 
    f"The dominant emotion is {res['dominant_emotion']}")

@app.route("/")
def render_index_page():
    """render the index page"""
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
