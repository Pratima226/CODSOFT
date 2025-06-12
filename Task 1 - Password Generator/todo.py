
import json
import os


class TodoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for idx, task in enumerate(self.tasks, 1):
            status = "✅" if task["done"] else "❌"
            print(f"{idx}. {task['task']} [{status}]")

    def mark_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["done"] = True
            self.save_tasks()
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")


def main():
    todo = TodoList()
    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.list_tasks()
        elif choice == "3":
            todo.list_tasks()
            try:
                num = int(input("Task number to mark done: ")) - 1
                todo.mark_done(num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            todo.list_tasks()
            try:
                num = int(input("Task number to delete: ")) - 1
                todo.delete_task(num)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
