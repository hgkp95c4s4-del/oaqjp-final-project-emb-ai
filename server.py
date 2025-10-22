"""
This application detects emotion/sentiment in a user prompt. 
"""

import requests
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

def run_app():
    """
    This is the portion of the application to define host and port parameters
    """
    app.run(host="localhost", port="5000")

@app.route("/emotionDetector")
def detect_emotion():
    """
    This component takes user input and assesses the emotion/sentiment
    and returns it to the user
    """
    user_input = request.args.get("textToAnalyze")
    response = emotion_detector(user_input)

    try:
        output = (f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']} 'fear': {response['fear']} 'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}")

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            output = "Invalid text! Please try again!"

    return output

@app.route("/")
def render_home():
    """
    This is the main insertion point for the application, loads the index.html on navigate
    """
    return render_template("index.html")

if __name__ == "__main__":
    run_app()
