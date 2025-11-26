import json
import os

TASK_FILE="task.json"



def load_task():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE) as file:

        try :
            return json.load(file)
        except json.JSONDecodeError :
            return [] 
tasks=load_task()
for t in tasks:
    print (t)

print("script startedT")