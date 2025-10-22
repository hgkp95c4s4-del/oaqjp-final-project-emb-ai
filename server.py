from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

def run_app():
    app.run(host="localhost", port="5000")

@app.route("/emotionDetector")
def detect_emotion():
    input = request.args.get("textToAnalyze")
    response = emotion_detector(input)

    try:
        output = f"For the given statement, the system response is 'anger': " + response['anger'],"
                f" 'disgust': " + response['disgust'] + f"'fear': " + response['fear'] + f" 'joy': "
                + response['joy'] + f" 'sadness':" + response['sadness'] + f". The dominant emotion is "
                + response['dominant_emotion']
    except:
        output = "Invalid text! Please try again!"
    finally:
        continue

@app.route("/")
def render_home:
    return render_template("index.html")

if __name__ == "__main__":
    run_app()