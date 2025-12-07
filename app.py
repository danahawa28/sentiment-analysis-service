
from flask import Flask, request, jsonify
from model import load_model, predict_text

app = Flask(__name__)
model = load_model()

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]
    prediction = predict_text(model, text)
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
