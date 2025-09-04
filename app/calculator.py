def calculate(a: float, b: float, op: str):
    if op == "add":
        return {"result": a + b}
    elif op == "sub":
        return {"result": a - b}
    elif op == "mul":
        return {"result": a * b}
    elif op == "div":
        return {"result": a / b if b != 0 else "Error: Division by zero"}
    else:
        return {"error": "Invalid operation"}
