from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve
import pickle

app = Flask(__name__)
CORS(app)  # Automatically enables CORS for all routes

# Load model and vectorizer
with open("sentiment_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    text = data.get("text")
    print(f"Received text: {text}")  # Debugging log
    
    transformed_text = vectorizer.transform([text])
    prediction = model.predict(transformed_text)[0]
    
    response = jsonify({"sentiment": int(prediction)})
    print(f"Prediction: {prediction}")  # Debugging log
    
    return response

if __name__ == "__main__":
    print("Starting server on port 8080...")  # Debugging log
    serve(app, host="0.0.0.0", port=8080)
