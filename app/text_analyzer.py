from collections import Counter
from .file_reader import read_file

def analyze_text(path):
    result = read_file(path)
    if "error" in result:
        return result
    
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
