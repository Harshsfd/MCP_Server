from fastapi import APIRouter
from .calculator import calculate
from .file_reader import read_file
from .text_analyzer import analyze_text
from .todo_manager import create_task, get_tasks, get_task, update_task, delete_task

router = APIRouter()

# ---- Calculator ----
@router.get("/calculate")
def calculate_route(a: float, b: float, op: str):
    return calculate(a, b, op)

# ---- File Reader ----
@router.get("/read_file")
def read_file_route(path: str):
    return read_file(path)

# ---- Text Analyzer ----
@router.get("/analyze_text")
def analyze_text_route(path: str):
    return analyze_text(path)

# ---- Todo Manager ----
@router.post("/todos/create")
def create_task_route(title: str, description: str = ""):
    return create_task(title, description)

@router.get("/todos")
def get_tasks_route():
    return get_tasks()

@router.get("/todos/{task_id}")
def get_task_route(task_id: int):
    return get_task(task_id)

@router.put("/todos/{task_id}")
def update_task_route(task_id: int, title: str = None, description: str = None, done: bool = None):
    return update_task(task_id, title, description, done)

@router.delete("/todos/{task_id}")
def delete_task_route(task_id: int):
    return delete_task(task_id)



@router.get("/.well-known/mcp/server-card")
def server_card():
    return {
        "server_name": "Local Multitask MCP Server",
        "host": "https://mcp-server-qko7.onrender.com",
        "version": "0.1",
        "tools": [
            {
                "name": "calculate",
                "path": "/calculate",
                "method": "GET",
                "description": "Basic arithmetic operations",
                "params": [{"name":"a","type":"number"},{"name":"b","type":"number"},{"name":"op","type":"string"}],
                "param_schema_depth": 1,
                "avg_tokens_estimate": 10,        # developer-provided estimate
                "sample_output": {"result": 3}
            },
            {
                "name":"read_file",
                "path":"/read_file",
                "method":"GET",
                "description":"Return file contents",
                "params":[{"name":"path","type":"string"}],
                "param_schema_depth":1,
                "avg_tokens_estimate":4000
            },
            ...
        ]
    }
