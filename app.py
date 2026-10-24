
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the saved model and TF-IDF vectorizer
artifacts = joblib.load("spam_detector.pkl")
model = artifacts["model"]
tfidf = artifacts["tfidf"]


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    message = ""

    if request.method == "POST":
        message = request.form.get("message", "").strip()

        if message:
            features = tfidf.transform([message])
            result = model.predict(features)[0]

            prediction = "SPAM" if result == 1 else "NOT SPAM"

    return render_template(
        "index.html",
        prediction=prediction,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)
