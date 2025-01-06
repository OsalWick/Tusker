# main.py

from task_handler import TaskHandler

def display_menu():
    print("\n=== Task Manager ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    print("=================")

def main():
    task_handler = TaskHandler()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            task_handler.add_task(title, description)
            print("Task added successfully!")
            
        elif choice == "2":
            tasks = task_handler.get_all_tasks()
            if not tasks:
                print("No tasks found!")
            else:
                print("\nYour Tasks:")
                for task in tasks:
                    print(f"\nID: {task['id']}")
                    print(f"Title: {task['title']}")
                    print(f"Description: {task['description']}")
                    print(f"Status: {'✓ Done' if task['completed'] else '○ Pending'}")
                    
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()