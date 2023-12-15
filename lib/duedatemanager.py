import datetime

class DueDateManager:
    def __init__(self):
        self.due_dates = {}
 # Define a due date for a task
    def set_due_date(self, task_id, due_date):
        self.due_dates[task_id] = due_date

    def get_due_date(self, task_id):
        return self.due_dates.get(task_id)

    def remove_due_date(self, task_id):
        if task_id in self.due_dates:
            del self.due_dates[task_id]

    def clear_all_due_dates(self):
        self.due_dates.clear()

    def get_overdue_tasks(self, current_date):
        overdue_tasks = [task_id for task_id, due_date in self.due_dates.items() if due_date < current_date]
        return overdue_tasks

    def get_upcoming_tasks(self, current_date, days_ahead):
        upcoming_tasks = {task_id: due_date for task_id, due_date in self.due_dates.items() if current_date < due_date <= current_date + datetime.timedelta(days=days_ahead)}
        return upcoming_tasks
