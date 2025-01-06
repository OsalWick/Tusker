# task_handler.py

class TaskHandler:
    def __init__(self):
        # Initialize an empty list to store tasks
        self.tasks = []
    
    def add_task(self, title, description=""):
        # Create a new task dictionary
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "completed": False
        }
        self.tasks.append(task)
        return task
    
    def get_all_tasks(self):
        # Return all tasks
        return self.tasks