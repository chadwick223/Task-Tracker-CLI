🚀 Task CLI — Command Line Task Manager

A simple and lightweight task manager built using Python.
Manage your to-dos directly from the terminal — add, list, update, and delete tasks with clean, readable output.

✨ Features

📌 Add new tasks

📋 List all tasks

🔍 Filter tasks by status

✏️ Update task status

❌ Delete tasks

💾 JSON-based storage (no database required)

⚡ Works on Windows, Mac, and Linux

📦 Installation (Windows Friendly)
1. Clone the Repository
git clone https://github.com/<chadwick223>/task-cli.git
cd task-cli
2. Install Python (if not already installed)

Download from: https://www.python.org/downloads/

Make sure to tick: "Add Python to PATH"

3. You're ready!

No virtual environment required.
No external dependencies.

🎮 Usage

Your CLI is executed using:

python Task_cli.py <command> <arguments>

🧩 Core Commands
1️⃣ Add a Task

Adds a new task with status TODO.

python Task_cli.py add "Buy groceries"
<img width="797" height="543" alt="image" src="https://github.com/user-attachments/assets/43152679-31b7-4967-bb35-246f34d1d6dd" />



Output:

Task added successfully

2️⃣ List All Tasks
python Task_cli.py list


Example output:
<img width="895" height="597" alt="image" src="https://github.com/user-attachments/assets/90ef76e7-033c-442d-91b8-5a2b17a4e20f" />



3️⃣ List Tasks by Status
python Task_cli.py list TODO
python Task_cli.py list DONE
<img width="1160" height="397" alt="image" src="https://github.com/user-attachments/assets/df9602a1-d1f3-4fa2-a30e-79b1b5c7ccc1" />

4️⃣ Update Task Status
python Task_cli.py update 4 TODO
<img width="1676" height="518" alt="image" src="https://github.com/user-attachments/assets/bc213197-6f5f-41a6-98ae-f4c65a21ce95" />




Output:

Task 4 updated successfully

5️⃣ Delete a Task
python Task_cli.py delete 4
<img width="1457" height="538" alt="image" src="https://github.com/user-attachments/assets/08aa2342-1f91-4049-9198-96c313067e83" />



Output:

Task 4 deleted successfully

📁 Project Structure
task-cli/
│── Task_cli.py      # Main CLI script
│── task.json        # Auto-generated storage file
│── README.md        # Documentation

🛠 Code Overview

Here are the major functions used in your app:

load_task() → loads JSON file

add_tasks() → adds a new task

save_tasks() → writes tasks to file

search_task() → finds a task by ID

update_task() → updates task status

delete_tasks() → deletes a task

list_tasks() → prints tasks (optionally filtered)

🧪 Example Workflow
python Task_cli.py add "Study Python"
python Task_cli.py add "Go to gym"
python Task_cli.py list
python Task_cli.py update 2 DONE
python Task_cli.py delete 1

🔧 Troubleshooting
❗ “python not recognized”

Install Python again and enable: Add Python to PATH

❗ “KeyError: 'staus'”

This is because of a typo in your code:

Change:

task["staus"]


to:

task["status"]



















