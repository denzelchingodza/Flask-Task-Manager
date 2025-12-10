import heapq
from task_model import Task

class Scheduler:
    def __init__(self):
        self.task_queue = []

    def add_task(self, task):
        heapq.heappush(self.task_queue, (-task.priority, task))
        return f"Task '{task.description}' added."

    def get_next_task(self):
        if not self.task_queue:
            return None
        _, task = heapq.heappop(self.task_queue)
        return task

    def get_all_tasks(self):
        # Return tasks sorted by priority
        return [task for _, task in sorted(self.task_queue, reverse=True)]

    def save_to_file(self, filename="tasks.txt"):
        with open(filename, "w") as f:
            for priority, task in sorted(self.task_queue, reverse=True):
                f.write(f"{task.description},{task.due_date},{task.priority},{task.estimated_time}\n")

    def load_from_file(self, filename="tasks.txt"):
        try:
            with open(filename, "r") as f:
                for line in f:
                    description, due_date, priority, estimated_time = line.strip().split(",")
                    task = Task(description, due_date, int(priority), float(estimated_time))
                    self.add_task(task)
        except FileNotFoundError:
            pass
