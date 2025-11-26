import json
import os
from datetime import datetime
import argparse
parser=argparse.ArgumentParser(description="Task manager cli")

parser.add_argument("command", help="Command to run")

parser.add_argument("value",nargs="?", help="value for Command")

parser.add_argument("extra",nargs="?", help="Extra argument")


args = parser.parse_args()

TASK_FILE="task.json"



def load_task():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE) as file:

        try :
            return json.load(file)
        except json.JSONDecodeError :
            return []
        
# load_task will return me the list of dictionary

def add_tasks(description,tasks):
    # if im creating a task , i need its id, its description, its status. at the time of creation, the status should be to do
    # and at the time of creation it should also have created at and updated at
    # can there be a way that as soon as i create task, or call create task. then automatically
    # {id , description,status,created at,  updated at, } keys are generated, and then i give input in an array and all those
    # element are mapped with keys
    if not tasks:
        taskid=1
    else:
        heighest=0
        for task in tasks:
            if task["id"]>heighest:
                heighest = task["id"]
        taskid=heighest+1
    timestamp=datetime.now().strftime("%y/%m/%d %I:%M %p")
    new_task={
        "id":taskid,
        "description":description,
        "status":"TODO",
        "createdAt":timestamp,
        "updatedAt":timestamp
    }
    tasks.append(new_task)
    #when i append a new task it is stored in ram ,i.e the temporary memory not on jason.
    save_tasks(tasks)
    #first thing i need to check is if that task is present in my jason or not 
    # if it is present , then I'll return some thing , else i'll add
def save_tasks(tasks):
    with open(TASK_FILE,"w") as file:
        json.dump(tasks,file,indent=4)
def search_task(id,tasks):
    for task in tasks:
        if task["id"]==id:
            return task
    return None

def update_task(id,tasks,status):
    result=search_task(id,tasks)
    if result ==None:
        return None
    else:
        result["status"]=status
        result["updatedAt"]=datetime.now().strftime("%y/%m/%d %I:%M %p")

    save_tasks(tasks)
def delete_tasks(id,tasks):
    result=search_task(id,tasks)
    if result == None:
        return "Task not found"
    else:
        tasks.remove(result)
    save_tasks(tasks)
    return f"Task {id} deleted successfully"


def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        print(f"ID         : {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status     : {task['status']}")
        print(f"Created At : {task['createdAt']}")
        print(f"Updated At : {task['updatedAt']}")
        print("-" * 40)


tasks=load_task()

if args.command=="add":
    description=args.value
    add_tasks(description,tasks)
    print("Task added successfully")
elif args.command=="list":
    print(list_tasks(tasks))
elif args.command=="delete":
    task_id=int(args.value)
    print(delete_tasks(task_id,tasks))
elif args.command == "update":
    task_id=int(args.value)
    status=args.extra
    print(update_task(task_id,tasks,status))
else:
    print("unknown command")
