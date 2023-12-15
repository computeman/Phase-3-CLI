class PriorityManager:
    def __init__(self):
        self.tasks = {}

    def set_task_priority(self, task_id, priority):
        self.tasks[task_id] = priority

    def get_task_priority(self, task_id):
        return self.tasks.get(task_id)

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]

    def clear_all_tasks(self):
        self.tasks.clear()
        
# Retrieve the task with the highest priority
    def get_highest_priority_task(self):
        if self.tasks:
            return max(self.tasks, key=self.tasks.get)
        else:
            return None
