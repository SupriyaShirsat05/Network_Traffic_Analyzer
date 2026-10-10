
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

MODEL_PATH = Path(__file__).with_name("model.pkl")
model = joblib.load(MODEL_PATH)

LABELS = {
    0: "Normal",
    1: "SYN Flood",
    2: "ACK Flood",
    3: "FIN Flood",
}

COLUMNS = ["frame.time_relative", "tcp.dstport", "frame.len"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Send a JSON object."}), 400

    features = data.get("features")

    if not isinstance(features, list) or len(features) != 3:
        return jsonify({
            "error": "features must contain exactly 3 numeric values."
        }), 400

    try:
        values = [float(value) for value in features]
        if not all(pd.notna(value) and abs(value) != float("inf")
                   for value in values):
            raise ValueError
    except (TypeError, ValueError):
        return jsonify({"error": "All features must be finite numbers."}), 400

    try:
        df = pd.DataFrame([values], columns=COLUMNS)
        prediction = int(model.predict(df)[0])
    except Exception:
        app.logger.exception("Prediction failed")
        return jsonify({"error": "Prediction failed."}), 500

    if prediction not in LABELS:
        return jsonify({"error": "Unexpected model prediction."}), 500

    return jsonify({
        "class_id": prediction,
        "label": LABELS[prediction],
    })


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(__import__("os").environ.get("PORT", 5000)),
        debug=False,
    )
