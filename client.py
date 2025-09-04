import requests

BASE_URL = "http://127.0.0.1:8000"

# ---- Calculator ----
def calc(a, b, op):
    response = requests.get(f"{BASE_URL}/calculate", params={"a": a, "b": b, "op": op})
    print("Calculator Result =>", response.json())

# ---- File Reader ----
def read_file(path):
    response = requests.get(f"{BASE_URL}/read_file", params={"path": path})
    print("File Reader Result =>", response.json())

# ---- Text Analyzer ----
def analyze(path):
    response = requests.get(f"{BASE_URL}/analyze_text", params={"path": path})
    print("Text Analyzer Result =>", response.json())

# ---- Todo Manager ----
def create_todo(title, description=""):
    response = requests.post(f"{BASE_URL}/todos/create", params={"title": title, "description": description})
    print("Create Task =>", response.json())

def get_all_todos():
    response = requests.get(f"{BASE_URL}/todos")
    tasks = response.json()
    print("All Tasks =>", tasks)
    return tasks

def update_todo(task_id, title=None, description=None, done=None):
    params = {}
    if title: params["title"] = title
    if description: params["description"] = description
    if done is not None: params["done"] = done
    response = requests.put(f"{BASE_URL}/todos/{task_id}", params=params)
    print(f"Update Task {task_id} =>", response.json())

def delete_todo(task_id):
    response = requests.delete(f"{BASE_URL}/todos/{task_id}")
    print(f"Delete Task {task_id} =>", response.json())

# ---- Interactive Todo Menu ----
def todo_manager():
    while True:
        print("\n--- Todo Manager ---")
        print("1. Create Task")
        print("2. View All Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("0. Back to Main Menu")
        choice = input("Choice: ")

        if choice == "1":
            title = input("Task title: ")
            description = input("Description: ")
            create_todo(title, description)
        elif choice == "2":
            get_all_todos()
        elif choice == "3":
            tasks = get_all_todos()
            try:
                task_id = int(input("Enter Task ID to update: "))
                title = input("New title (leave blank to keep current): ")
                description = input("New description (leave blank to keep current): ")
                done_input = input("Mark done? (y/n/leave blank to keep current): ").lower()
                done = None
                if done_input == "y":
                    done = True
                elif done_input == "n":
                    done = False
                update_todo(task_id, title if title else None, description if description else None, done)
            except ValueError:
                print("Invalid ID")
        elif choice == "4":
            tasks = get_all_todos()
            try:
                task_id = int(input("Enter Task ID to delete: "))
                confirm = input(f"Are you sure you want to delete Task {task_id}? (y/n): ").lower()
                if confirm == "y":
                    delete_todo(task_id)
            except ValueError:
                print("Invalid ID")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

# ---- Main Menu ----
def main_menu():
    while True:
        print("\n--- MCP Tools Menu ---")
        print("1. Calculator")
        print("2. File Reader")
        print("3. Text Analyzer")
        print("4. Todo Manager")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            op = input("Operation (add/sub/mul/div): ")
            calc(a, b, op)
        elif choice == "2":
            path = input("Enter file path: ")
            read_file(path)
        elif choice == "3":
            path = input("Enter file path: ")
            analyze(path)
        elif choice == "4":
            todo_manager()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main_menu()
