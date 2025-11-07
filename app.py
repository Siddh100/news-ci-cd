from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "368ce959f5f840449f21d4f03811e590"  # <-- Your new key INSIDE quotes


@app.route("/")
def home():
    url = "https://newsapi.org/v2/top-headlines?country=us"

    headers = {
        "X-Api-Key": API_KEY  # <-- Important: Use headers (not url param)
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    if data.get("status") != "ok":
        return "Error fetching news: " + str(data.get("message"))

    articles = data.get("articles", [])
    return render_template("index.html", articles=articles)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
