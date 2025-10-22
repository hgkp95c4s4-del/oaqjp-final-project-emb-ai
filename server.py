from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

def run_app():
    app.run(host="localhost", port="5000")

