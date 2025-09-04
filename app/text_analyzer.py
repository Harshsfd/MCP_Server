from collections import Counter
from .file_reader import read_file  # Ensure file_reader.py same folder me ho

def analyze_text(path):
    result = read_file(path)
    
    # Agar file read me error aaye ya file exist na kare
    if "error" in result:
        return {"error": "Data not found"}  # <- ye line update hui
    
    content = result["content"]
    lines = content.splitlines()
    words = content.split()
    characters = len(content)
    
    most_common_words = Counter(words).most_common(5)
    
    return {
        "lines": len(lines),
        "words": len(words),
        "characters": characters,
        "most_common_words": most_common_words
    }
