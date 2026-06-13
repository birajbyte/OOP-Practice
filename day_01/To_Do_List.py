# Todo List with priorities:
# Classes needed:
# →  Task class
class Task:
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
        self.status = "pending"
class TodoList:
    def __init__(self,name):
        self.tasks= []
        self.name = name
    def add_task(self,task):
        self.tasks.append(task)
        print("Task Added Successfully")
    def show_all(self):
        if not self.tasks:
            print("Add task in to_do_List")
            return
        else:
            for task in self.tasks:
                print(f"\nTask:{task.title}|Priority:{task.priority}")
    def show_priority(self):
        order = input("The priority order: ").lower()
        seen = {"high","low","medium"}
        if not self.tasks:
            print("ADD Task first!")
            return
        elif order not in seen:
            print("invalid input")
        else:
            for task in self.tasks:
                if task.priority.lower() == order:
                    print(f"\nTask:{task.title}|Priority:{task.priority}")
            
    def show_pending(self):
        if not self.tasks:
            print("Add task first!")
            return
        else:
            for task in self.tasks:
                if task.status == "pending":
                    print(f"{task.title}:{task.priority}:{task.status}\n")
            
    def complete_task(self,title):
        if not self.tasks:
            print("Add task first!")
            return
        else:
            for task in self.tasks:
                if task.title.lower() == title.lower():
                    task.status = "completed"
                    print(f"{title} task completed\n")
                    break
            else:
                print("Task NOt Found")
Biraj = TodoList("Biraj")     
Biraj.add_task(Task("Learn OOP", "high"))
Biraj.add_task(Task("Do Math", "high"))
Biraj.add_task(Task("Watch reels", "low")) 
Biraj.add_task(Task("Build project", "high"))
Biraj.add_task(Task("Exercise", "medium"))

Biraj.show_all()
Biraj.complete_task("Learn OOP")
Biraj.show_pending()
Biraj.show_priority()
        
# →  TodoList class  ← composition!
# Task has:
# →  priority (high/medium/low)
# →  status (pending/done)
# TodoList has:
# →  list of Task objects
# →  add_task()
# →  complete_task()
# →  show_all()
# →  show_by_priority()
# →  show_pending()

