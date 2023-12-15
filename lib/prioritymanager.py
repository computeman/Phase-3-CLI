class PriorityManager:
    def __init__(self):
        self.tasks = {}

    def set_task_priority(self, task_id, priority):
        # Assign a priority level to a task
        self.tasks[task_id] = priority

    def get_task_priority(self, task_id):
        # Retrieve the priority level of a task
        return self.tasks.get(task_id)

    def remove_task(self, task_id):
        # Remove a task from the priority manager
        if task_id in self.tasks:
            del self.tasks[task_id]

    def clear_all_tasks(self):
        # Clear all tasks from the priority manager
        self.tasks.clear()

    def get_highest_priority_task(self):
        # Retrieve the task with the highest priority
        if self.tasks:
            return max(self.tasks, key=self.tasks.get)
        else:
            return None
