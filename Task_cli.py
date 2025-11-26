import json
import os
from datetime import datetime
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
    save_tasks(tasks)
    #first thing i need to check is if that task is present in my jason or not 
    # if it is present , then I'll return some thing , else i'll add
def save_tasks(tasks):
    with open(TASK_FILE,"w") as file:
        json.dump(tasks,file,indent=4)
     
tasks=load_task()

add_tasks("outing",tasks)
tasks=load_task()
print(tasks)
#print("script startedT")