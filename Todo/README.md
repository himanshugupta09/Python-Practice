# 📝 To-Do List Manager (Python)

A simple command-line **To-Do List Manager** built with Python that allows users to manage their daily tasks. Tasks are stored persistently in a JSON file, making them available even after the program exits.

---

## ✨ Features

* ➕ Add new tasks
* ✏️ Update existing tasks
* 🗑️ Delete tasks
* 📋 View all active (incomplete) tasks
* 💾 Persistent storage using `data.json`
* 🖥️ Easy-to-use command-line interface

---

## 📂 Project Structure

```
todo-list/
│
├── main.py          # Main application
├── data.json        # Stores all tasks
└── README.md        # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or above

### Clone the Repository

```bash
git clone https://github.com/your-username/todo-list.git
cd todo-list
```

### Run the Application

```bash
python main.py
```

---

## 📌 Menu Options

When you run the program, you'll see:

```
1. Add Task
2. Update Task
3. Delete Task
4. View Active Tasks
```

Type the corresponding number to perform an action.

To exit the application, type:

```
exit
```

---

## 🛠️ Functionality

### ➕ Add Task

Create a new task by entering:

* Title
* Description
* Deadline (YYYY-MM-DD)

Example:

```
Enter task title: Complete DSA
Enter task description: Solve Graph problems
Enter task deadline: 2026-07-01
```

---

### ✏️ Update Task

Update an existing task by entering:

* Task title
* Completion status
* New description (optional)
* New deadline (optional)

---

### 🗑️ Delete Task

Delete a task by providing its title.

Example:

```
Enter task title to delete: Complete DSA
```

---

### 📋 View Active Tasks

Displays every task whose completion status is **False**.

Example output:

```
Title: Complete DSA
Description: Solve Graph problems
Deadline: 2026-07-01
```

---

## 💾 Data Storage

All tasks are stored inside `data.json` in the following format:

```json
[
    {
        "title": "Complete DSA",
        "description": "Solve Graph problems",
        "deadline": "2026-07-01",
        "completed": false
    }
]
```

---

## 🏗️ Project Design

The application consists of two classes:

### `ToDo`

Represents a single task.

Attributes:

* `title`
* `description`
* `deadline`
* `completed`

### `TaskManager`

Handles all task operations:

* `add_task()`
* `update_task()`
* `delete_task()`
* `get_active_tasks()`

---

## 📚 Concepts Used

* Object-Oriented Programming (OOP)
* Classes & Objects
* JSON File Handling
* Lists & Dictionaries
* Exception Handling
* Conditional Statements
* Loops
* File I/O

---

## 🔮 Future Improvements

* ✅ View all tasks (completed + pending)
* 🔍 Search tasks by title
* 📅 Sort tasks by deadline
* ⏰ Notify overdue tasks
* 🎨 Better CLI using `rich` or `colorama`
* 🔢 Task IDs instead of titles
* 📊 Progress statistics
* 🖥️ GUI version using Tkinter or PyQt
* 🌐 Web version using Flask or Django

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

---

## 📄 License

This project is open source and available under the **MIT License**.

---

## 👨‍💻 Author @HimanshuGupta09

Built with ❤️ using Python.
