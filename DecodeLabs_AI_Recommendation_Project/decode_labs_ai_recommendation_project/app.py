"""
DecodeLabs Project 3 — AI Recommendation Logic
A small Flask web app that recommends learning resources using tag similarity.
Run: pip install -r requirements.txt && python app.py
"""
from flask import Flask, render_template, request
from recommender import recommend, CATALOG, AVAILABLE_INTERESTS

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    selected = []
    results = []
    message = ""
    if request.method == "POST":
        selected = request.form.getlist("interests")
        if selected:
            results = recommend(selected, limit=6)
            if results:
                message = f"Found {len(results)} recommendations matched to your interests."
        else:
            message = "Please select at least one interest to get recommendations."
    return render_template(
        "index.html",
        interests=AVAILABLE_INTERESTS,
        selected=selected,
        results=results,
        message=message,
        catalog_count=len(CATALOG),
    )

if __name__ == "__main__":
    app.run(debug=True)
