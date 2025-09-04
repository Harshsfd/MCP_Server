# In-memory storage for tasks
tasks = []
task_id_counter = 1

def create_task(title, description=""):
    global task_id_counter
    task = {
        "id": task_id_counter,
        "title": title,
        "description": description,
        "done": False
    }
    tasks.append(task)
    task_id_counter += 1
    return task

def get_tasks():
    return tasks

def get_task(task_id):
    for t in tasks:
        if t["id"] == task_id:
            return t
    return {"error": "Task not found"}

def update_task(task_id, title=None, description=None, done=None):
    for t in tasks:
        if t["id"] == task_id:
            if title is not None:
                t["title"] = title
            if description is not None:
                t["description"] = description
            if done is not None:
                t["done"] = done
            return t
    return {"error": "Task not found"}

def delete_task(task_id):
    global tasks
    for t in tasks:
        if t["id"] == task_id:
            tasks = [task for task in tasks if task["id"] != task_id]
            return {"message": "Task deleted"}
    return {"error": "Task not found"}
