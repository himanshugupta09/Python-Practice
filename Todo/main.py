from datetime import datetime
import json
import os
class ToDo:
    def __init__(self,title,description,deadline,completed=False):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = completed
class TaskManager:
    def __init__(self):
        pass
    def add_task(self, task):
        date_format = "%Y-%m-%d"
        user_datetime = datetime.strptime(task.deadline, date_format)
        new_task = {
            "title": task.title,
            "description": task.description,
            "deadline": user_datetime.strftime(date_format),
            "completed": task.completed
        }

        if os.path.exists("data.json"):
            with open("data.json", "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        else:
            data = []

        data.append(new_task)

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

    def get_active_tasks(self):
        data = json.loads(open("data.json").read())
        for task in data:
            if not task["completed"]:
                print(f"Title: {task['title']}, Description: {task['description']}, Deadline: {task['deadline']}")
    def update_task(self, completed, title=None, description=None, deadline=None):
        with open("data.json", "r") as f:
                data = json.load(f)
        task_found = False
        for task in data:
            if task["title"] == title:
                task_found = True
                task["completed"] = completed
                if description:
                    task["description"] = description
                if deadline:
                    task["deadline"] = deadline
                break
        if task_found:
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)    
        


    def delete_task(self, title):
        with open("data.json", "r") as f:
            data = json.load(f)

        data = [task for task in data if task["title"] != title]

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

taskmanager = TaskManager()
q = input("Enter choice (1. Add Task, 2. Update Task, 3. Delete Task, 4. View Active Tasks): ")
while q != "exit":
    if q == "1":
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        deadline = input("Enter task deadline (YYYY-MM-DD): ")
        task = ToDo(title, description, deadline)
        taskmanager.add_task(task)
    elif q == "2":
        title = input("Enter task title to update: ")
        completed = input("Is the task completed? (yes/no): ").lower() == "yes"
        description = input("Enter new description (leave blank to keep current): ")
        deadline = input("Enter new deadline (YYYY-MM-DD) (leave blank to keep current): ")
        taskmanager.update_task(
                completed,
                title,
                description,
                deadline
            )
    elif q == "3":
        title = input("Enter task title to delete: ")
        taskmanager.delete_task(title)
    elif q == "4":
        taskmanager.get_active_tasks()
    else:
        print("Invalid choice. Please try again.")
    
    q = input("Enter choice (1. Add Task, 2. Update Task, 3. Delete Task, 4. View Active Tasks): ")

    
