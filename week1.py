class Task:
    def __init__(self, description, due_date=None, priority=0):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def complete(self):
        self.completed = True

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, description, due_date=None, priority=0):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def display_tasks(self):
        for idx, task in enumerate(self.tasks):
            print(f"{idx + 1}. {task.description} - Due: {task.due_date} - Priority: {task.priority}")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            task.complete()
            self.completed_tasks.append(task)
            self.tasks.remove(task)

    def update_task(self, task_number, description=None, due_date=None, priority=None):
        if 1 <= task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            if description:
                task.description = description
            if due_date:
                task.due_date = due_date
            if priority:
                task.priority = priority

    def remove_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            del self.tasks[task_number - 1]

    def display_completed_tasks(self):
        for idx, task in enumerate(self.completed_tasks):
            print(f"{idx + 1}. {task.description} - Due: {task.due_date} - Priority: {task.priority}")

def main():
    todo_list = ToDoList()
    while True:
        print("\n1. Add Task\n2. Display Tasks\n3. Mark Task Completed\n4. Update Task\n5. Remove Task\n6. Display Completed Tasks\n7. Exit")
        option = int(input("Choose an option: "))
        if option == 1:
            description = input("Enter task description: ")
            due_date = input("Enter task due date (optional): ")
            priority = int(input("Enter task priority (optional): "))
            todo_list.add_task(description, due_date, priority)
        elif option == 2:
            todo_list.display_tasks()
        elif option == 3:
            task_number = int(input("Enter task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif option == 4:
            task_number = int(input("Enter task number to update: "))
            description = input("Enter new task description (optional): ")
            due_date = input("Enter new task due date (optional): ")
            priority = int(input("Enter new task priority (optional): "))
            todo_list.update_task(task_number, description, due_date, priority)
        elif option == 5:
            task_number = int(input("Enter task number to remove: "))
            todo_list.remove_task(task_number)
        elif option == 6:
            todo_list.display_completed_tasks()
        elif option == 7:
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()