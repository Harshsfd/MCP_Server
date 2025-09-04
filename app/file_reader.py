def read_file(path):
    try:
        with open(path, "r") as f:
            content = f.read()
        return {"content": content}
    except FileNotFoundError:
        return {"error": "File not found"}
    except Exception as e:
        return {"error": str(e)}
