import os

def read_file(path: str):
    if os.path.exists(path):
        with open(path, "r") as f:
            content = f.read()
        return {"content": content}
    else:
        return {"error": "File not found"}
