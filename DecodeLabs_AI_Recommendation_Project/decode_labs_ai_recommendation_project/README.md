# DecodeLabs Project 3 — AI Recommendation Logic

A GitHub-ready mini project that recommends learning resources based on a user's interests. It follows the brief's core requirements: accept user choices, match preferences using similarity logic, and display ranked recommendations.

## Features

- Select multiple interests from a clean, responsive web interface.
- Content-based recommendation using item tags.
- Jaccard similarity score displayed as a percentage.
- Recommendations sorted by score, with a stable alphabetical tie-breaker.
- Shows matched tags so the result is explainable.
- Includes a small sample catalog of courses, tutorials, and projects.
- Standalone Python logic that can be tested or reused without the web app.

## Tech stack

- Python 3.10+
- Flask
- HTML and CSS

## Run locally

1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (recommended):

   **Windows**
   ```powershell
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Open http://127.0.0.1:5000 in your browser.

## How the recommendation logic works

Each catalog item has a set of tags. The user selects interest tags. For each item, the app calculates Jaccard similarity:

`similarity = |user interests ∩ item tags| / |user interests ∪ item tags| × 100`

Items with at least one matching tag are ranked from highest to lowest score. If scores tie, titles are sorted alphabetically. This is an explainable, content-based baseline—not a trained machine-learning model.

## Try the logic without starting Flask

```bash
python recommender.py
```

Or use the functions in your own script:

```python
from recommender import recommend

for item in recommend(["python", "ai"], limit=5):
    print(item["title"], item["score"], item["matched_tags"])
```

## Project structure

```text
decode-labs-ai-recommendation-project/
├── app.py
├── recommender.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Upload to GitHub

Create a new **public** repository on GitHub (for example, `decodelabs-ai-recommendation-project`). Do not initialize it with a README if you plan to push this folder as-is. In the terminal, from this folder run:

```bash
git init
git add .
git commit -m "Complete DecodeLabs AI recommendation project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/decodelabs-ai-recommendation-project.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If Git says the remote already exists, use `git remote set-url origin https://github.com/YOUR-USERNAME/decodelabs-ai-recommendation-project.git`.

## Scope and limitations

The included catalog is sample data created for this project. Recommendations depend on shared tags, so results are only as good as the tags and catalog. No personal data is saved, and no external recommendation API is used.

## Project brief

**Goal:** Create a simple recommendation system based on user preferences.

**Key requirements:** Take user input (choices or interests), match preferences using logic or similarity, and display recommended items.

**Skills demonstrated:** Logic building, pattern matching, and recommendation concepts.
