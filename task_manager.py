import json

tasks = []
deadlines = {}
#Create different functions

def displayTask(all_tasks, deadlines):
     print("\nYour Task: ")
     if len(all_tasks) <= 0:
          print("No tasks!")
     else:
          for index, task in enumerate(all_tasks):
               print(f"{index+1}: {task} - {deadlines[task]}")

def newOperation(all_tasks, deadlines):
     print(deadlines)
     operation = input("Press:\n'A' to add a new task\n'E' to edit a task\n'R' to remove a task\n'S' to save tasks\n'F' to Quit: ").lower()

     if operation == "a":
          addTask(all_tasks, deadlines)
     elif operation == "e":
          editTask(all_tasks, deadlines)
     elif operation == "r":
          removeTask(all_tasks, deadlines)
     elif operation == "s":
          saveTask(all_tasks, deadlines)
     elif operation == "l":
          loadTask(all_tasks, deadlines)
     elif operation == "f":
          return
     else:
          newOperation(all_tasks, deadlines)

def validTaskNumber(all_tasks, operation):
     task_number = input(f"Enter the number you want to {operation}: ")

     valid = False
     while not valid:
          try:
               number = int(task_number)
               valid = True
          except:
               task_number = input("Please enter a valid task number! ")
     if not (0 < number <= len(all_tasks)):
          print("Task not found! ")
          validTaskNumber(all_tasks, operation)
     else:
          return number
 

#Operations
def addDeadlines(task, deadlines):
     deadline = input("Enter a deadline: ")
     deadlines[task] = deadline
     return deadlines

def editTask(all_tasks, deadlines):
     task_number = validTaskNumber(all_tasks, "Edit")

     new_task = input("Edit task: ")
     old_task = all_tasks[task_number-1]
     all_tasks[task_number-1] = new_task
     #If the task name change, update the deadlines
     deadlines[new_task] = deadlines.pop(old_task)

     #ask the user if they want to edit the deadlines as well
     edit_deadline = input("Do you want to edit the deadline as well(yes or no): ").lower()
     if edit_deadline == "yes":
          addDeadlines(new_task, deadlines)
     print(f"Item {task_number} id updated!")
     displayTask(all_tasks, deadlines)
     newOperation(all_tasks, deadlines)

def removeTask(all_tasks, deadlines):
     task_number = validTaskNumber(all_tasks, "Remove")

     del deadlines[all_tasks[task_number-1]]
     all_tasks.pop(task_number-1)
     print(f"Item {task_number} is removed!")

     displayTask(all_tasks, deadlines)
     newOperation(all_tasks, deadlines)

def addTask(all_tasks, deadlines):
     new_task = input("Add task: ")
     all_tasks.append(new_task)
     addDeadlines(new_task, deadlines)

     displayTask(all_tasks, deadlines)
     newOperation(all_tasks, deadlines)

#Save tasks to a JSON file
def saveTask(all_tasks, deadlines):
     data = {
          "tasks": tasks,
          "deadlines": deadlines
     }
     with open("tasks.json","w") as file:
          json.dump(data, file ,indent=4)
     print("Tasks saved to a Json file as tasks.json")
     newOperation(all_tasks, deadlines)

def loadTask(all_tasks, deadlines):
     try:
          with open("tasks.json","r") as file:
               data = json.load(file)
               all_tasks.clear()
               all_tasks.extend(data["tasks"])
               deadlines.clear()
               deadlines.update(data["deadlines"])
          print("Task loaded from a json file")
     except FileNotFoundError:
          print("No  saved file as tasks.json")

     displayTask(all_tasks, deadlines)
     newOperation(all_tasks, deadlines)

# Run the application
newOperation(tasks, deadlines)