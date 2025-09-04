from fastapi import APIRouter
from .calculator import calculate
from .file_reader import read_file
from .text_analyzer import analyze_text
from .todo_manager import create_task, get_tasks, get_task, update_task, delete_task


router = APIRouter()


# Existing endpoints...
@router.get("/calculate")
def calculate_route(a: float, b: float, op: str):
    return calculate(a, b, op)

@router.get("/read_file")
def read_file_route(path: str):
    return read_file(path)

@router.get("/analyze_text")
def analyze_text_route(path: str):
    return analyze_text(path)

# ---- Todo Manager Endpoints ----

# Create task
@router.post("/todos/create")
def create_task_route(title: str, description: str = ""):
    return create_task(title, description)

# Get all tasks
@router.get("/todos")
def get_tasks_route():
    return get_tasks()

# Get single task by id
@router.get("/todos/{task_id}")
def get_task_route(task_id: int):
    return get_task(task_id)

# Update task
@router.put("/todos/{task_id}")
def update_task_route(task_id: int, title: str = None, description: str = None, done: bool = None):
    return update_task(task_id, title, description, done)

# Delete task
@router.delete("/todos/{task_id}")
def delete_task_route(task_id: int):
    return delete_task(task_id)
