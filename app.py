from flask import Flask, render_template, request
import pickle
import json

from tensorflow import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences

from pipeline import clean_text

app = Flask(__name__)

# ----------------------------
# Load model
# ----------------------------
model = keras.models.load_model("ai_human_gru_model_2.keras", compile=False)

# ----------------------------
# Load tokenizer
# ----------------------------
with open("tokenizer_2.pickle", "rb") as f:
    tokenizer = pickle.load(f)

# ----------------------------
# Load config
# ----------------------------
with open("config.json", "r") as f:
    config = json.load(f)

MAX_LEN = config["max_len"]


# ----------------------------
# Prediction function
# ----------------------------
def predict_text(text, threshold=0.5):

    # EXACT same preprocessing as notebook
    cleaned = clean_text(text)

    seq = tokenizer.texts_to_sequences([cleaned])

    padded = pad_sequences(
        seq,
        maxlen=MAX_LEN,
        padding="post",
        truncating="post"
    )

    prob = float(model.predict(padded, verbose=0)[0][0])

    ai_prob = prob
    human_prob = 1 - prob

    if prob >= threshold:
        label = "AI Generated"
        confidence = ai_prob
    else:
        label = "Human Written"
        confidence = human_prob

    confidence *= 100

    if confidence >= 99:
        level = "Very High"
    elif confidence >= 95:
        level = "High"
    elif confidence >= 80:
        level = "Medium"
    else:
        level = "Low"

    return {
        "prediction": label,
        "ai_prob": round(ai_prob * 100, 2),
        "human_prob": round(human_prob * 100, 2),
        "confidence": round(confidence, 2),
        "level": level,
    }


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        text = request.form.get("text", "").strip()

        if text:
            result = predict_text(text)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)