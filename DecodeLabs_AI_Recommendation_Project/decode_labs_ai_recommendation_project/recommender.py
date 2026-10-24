"""Content-based recommendation logic for DecodeLabs AI Project 3."""
from typing import Iterable

# Each item has tags that describe its topic and difficulty.
CATALOG = [
    {"id": 1, "title": "Python for Everybody", "category": "Course", "level": "Beginner",
     "description": "Build a strong foundation in Python, variables, loops, functions, and data structures.",
     "tags": {"python", "programming", "beginner", "data"}},
    {"id": 2, "title": "Data Analysis with Pandas", "category": "Tutorial", "level": "Intermediate",
     "description": "Clean, transform, explore, and summarize real-world datasets with Pandas.",
     "tags": {"python", "data", "analytics", "visualization"}},
    {"id": 3, "title": "Machine Learning Fundamentals", "category": "Learning Path", "level": "Beginner",
     "description": "Understand supervised learning, model evaluation, features, and training workflows.",
     "tags": {"ai", "machine learning", "python", "data"}},
    {"id": 4, "title": "Deep Learning Starter", "category": "Course", "level": "Intermediate",
     "description": "Explore neural networks, activation functions, backpropagation, and model training.",
     "tags": {"ai", "deep learning", "machine learning", "python"}},
    {"id": 5, "title": "Web Development with HTML & CSS", "category": "Project", "level": "Beginner",
     "description": "Create responsive web pages using semantic HTML, CSS layouts, and accessible design.",
     "tags": {"web development", "html", "css", "design", "beginner"}},
    {"id": 6, "title": "JavaScript Interactive Apps", "category": "Project", "level": "Intermediate",
     "description": "Add interactivity to websites with JavaScript events, functions, and DOM updates.",
     "tags": {"web development", "javascript", "programming"}},
    {"id": 7, "title": "SQL and Database Basics", "category": "Tutorial", "level": "Beginner",
     "description": "Learn queries, filtering, joins, grouping, and relational database concepts.",
     "tags": {"sql", "database", "data", "beginner"}},
    {"id": 8, "title": "Data Visualization Essentials", "category": "Learning Path", "level": "Beginner",
     "description": "Choose effective charts and communicate insights clearly from data.",
     "tags": {"data", "analytics", "visualization", "design"}},
    {"id": 9, "title": "Natural Language Processing", "category": "Course", "level": "Advanced",
     "description": "Work with text preprocessing, embeddings, sentiment analysis, and language models.",
     "tags": {"ai", "nlp", "machine learning", "python"}},
    {"id": 10, "title": "UI/UX Design Basics", "category": "Learning Path", "level": "Beginner",
     "description": "Practice user research, wireframing, visual hierarchy, and usability principles.",
     "tags": {"design", "ui ux", "web development", "beginner"}},
    {"id": 11, "title": "Git and GitHub Essentials", "category": "Tutorial", "level": "Beginner",
     "description": "Track changes, manage branches, write commits, and publish projects on GitHub.",
     "tags": {"programming", "github", "git", "beginner"}},
    {"id": 12, "title": "Computer Vision Basics", "category": "Course", "level": "Intermediate",
     "description": "Learn image preprocessing, classification, object detection, and vision workflows.",
     "tags": {"ai", "computer vision", "machine learning", "python"}},
]

AVAILABLE_INTERESTS = [
    ("ai", "Artificial Intelligence"), ("machine learning", "Machine Learning"),
    ("deep learning", "Deep Learning"), ("python", "Python"),
    ("data", "Data Science"), ("analytics", "Data Analytics"),
    ("visualization", "Data Visualization"), ("web development", "Web Development"),
    ("javascript", "JavaScript"), ("html", "HTML"), ("css", "CSS"),
    ("design", "Design"), ("ui ux", "UI/UX"), ("sql", "SQL & Databases"),
    ("github", "Git & GitHub"), ("nlp", "Natural Language Processing"),
    ("computer vision", "Computer Vision"), ("programming", "Programming"),
]

def _normalise(tags: Iterable[str]) -> set[str]:
    """Normalise user choices and item tags for consistent matching."""
    return {str(tag).strip().lower() for tag in tags if str(tag).strip()}

def similarity_score(user_interests: Iterable[str], item_tags: Iterable[str]) -> float:
    """
    Jaccard similarity: intersection / union, expressed as a percentage.
    Returns 0 when both sets are empty.
    """
    user_set, tag_set = _normalise(user_interests), _normalise(item_tags)
    union = user_set | tag_set
    if not union:
        return 0.0
    return round((len(user_set & tag_set) / len(union)) * 100, 1)

def recommend(user_interests: Iterable[str], limit: int = 6) -> list[dict]:
    """Return catalog items ranked by tag similarity, highest score first."""
    interests = _normalise(user_interests)
    if not interests:
        return []
    ranked = []
    for item in CATALOG:
        score = similarity_score(interests, item["tags"])
        if score > 0:
            ranked.append({**item, "score": score,
                           "matched_tags": sorted(interests & item["tags"])})
    ranked.sort(key=lambda item: (-item["score"], item["title"].lower()))
    return ranked[:max(0, limit)]

if __name__ == "__main__":
    demo = recommend(["python", "ai"], limit=5)
    print("Demo recommendations for interests: Python, AI")
    for item in demo:
        print(f"{item['score']:>5}%  {item['title']} — {item['description']}")
