from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Task


class SQLAlchemyPriorityManager:
    def __init__(self, engine_url="sqlite:///taskmanager.db"):
        self.engine = create_engine(engine_url)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def set_task_priority(self, task_id, priority):
        task = self.session.query(Task).get(task_id)
        if task:
            task.priority = priority
            self.session.commit()

    def get_task_priority(self, task_id):
        task = self.session.query(Task).get(task_id)
        if task:
            return task.priority
        return None

    def remove_task(self, task_id):
        task = self.session.query(Task).get(task_id)
        if task:
            self.session.delete(task)
            self.session.commit()

    # def clear_all_tasks(self):
    #     self.session.query(Task).delete()
    #     self.session.commit()

    def get_highest_priority_task(self):
        tasks_with_priority = (
            self.session.query(Task).filter(Task.priority.isnot(None)).all()
        )
        if tasks_with_priority:
            return max(
                tasks_with_priority,
                key=lambda task: self.priority_to_int(task.priority),
            )
        else:
            return None

    def priority_to_int(self, priority_str):
        priorities = {"Low": 1, "Medium": 2, "High": 3}
        return priorities.get(priority_str, 0)


# Example usage
if __name__ == "__main__":
    priority_manager = SQLAlchemyPriorityManager()

    # Set priority for a task
    priority_manager.set_task_priority(task_id=2, priority="High")

    # Get priority for a task
    priority = priority_manager.get_task_priority(task_id=3)
    print(f"Priority for task 1: {priority}")

    # Remove a task
    priority_manager.remove_task(task_id=4)
    print("Removed item");

    # # Clear all tasks
    # priority_manager.clear_all_tasks()

    # Get the task with the highest priority
    highest_priority_task = priority_manager.get_highest_priority_task()
    print(f"Highest priority task: {highest_priority_task}")
