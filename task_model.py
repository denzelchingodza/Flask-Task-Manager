# task_model.py

class Task:
    def __init__(self, description, due_date, priority, estimated_time):
        self.description = description 
        self.due_date = due_date
        self.priority = priority
        self.estimated_time = estimated_time

    def __str__(self):
        return (f"Task: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Priority: {self.priority}\n"
                f"Estimated Time: {self.estimated_time} hours\n")
