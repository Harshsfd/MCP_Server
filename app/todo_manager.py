# app/todo_manager.py
todos = []
next_id = 1

def create_task(title: str, description: str = ""):
    global next_id
    task = {"id": next_id, "title": title, "description": description, "done": True}
    todos.append(task)
    next_id += 1
    return task

def get_tasks():
    return todos

def get_task(task_id: int):
    for task in todos:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}

def update_task(task_id: int, title: str = None, description: str = None, done: bool = None):
    for task in todos:
        if task["id"] == task_id:
            if title is not None:
                task["title"] = title
            if description is not None:
                task["description"] = description
            if done is not None:
                task["done"] = done
            return task
    return {"error": "Task not found"}

def delete_task(task_id: int):
    global todos
    for task in todos:
        if task["id"] == task_id:
            todos = [t for t in todos if t["id"] != task_id]
            return {"message": "Task deleted"}
    return {"error": "Task not found"}
