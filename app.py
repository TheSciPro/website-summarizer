import os
from flask import Flask, render_template, request
from fetch_content import fetch_web_content
from summarize import generate_summary
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = None  
    if request.method == "POST":
        url = request.form.get("url")
        query = request.form.get("query", "")

        if not url:
            return render_template("index.html", summary="Please enter a valid URL.")

        page_content = fetch_web_content(url)
        if not page_content:
            return render_template("index.html", summary="Failed to extract content from the URL.")

        summary = generate_summary(page_content, query)

    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
