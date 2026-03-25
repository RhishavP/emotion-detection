from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text = request.args.get("textToAnalyze")

    if not text or text.strip() == "":
        return jsonify({"error": "Invalid input"}), 400

    try:
        result = emotion_detector(text)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)