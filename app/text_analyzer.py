from collections import Counter
import os

def analyze_text(path: str):
    if not os.path.exists(path):
        return {"error": "File not found"}

    with open(path, "r") as f:
        content = f.read()

    lines = content.split("\n")
    words = content.split()
    characters = len(content)

    # Most common words
    word_counts = Counter(words)
    most_common = word_counts.most_common(5)  # Top 5 words

    return {
        "lines": len(lines),
        "words": len(words),
        "characters": characters,
        "most_common_words": most_common
    }
