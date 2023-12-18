from sqlalchemy.orm import Session
from sqlalchemy import func
from models import Task
from datetime import timedelta
from datetime import datetime


class DueDateManager:
    def __init__(self, session: Session):
        self.session = session

    # Define a due date for a task
    def set_due_date(self, task_id, due_date):
        task = self.session.query(Task).filter_by(task_id=task_id).first()
        if task:
            task.due_date = due_date
            self.session.commit()

    def get_due_date(self, task_id):
        task = self.session.query(Task).filter_by(task_id=task_id).first()
        if task:
            return task.due_date
        return None

    def remove_due_date(self, task_id):
        task = self.session.query(Task).filter_by(task_id=task_id).first()
        if task and task.due_date:
            task.due_date = None
            self.session.commit()

    def clear_all_due_dates(self):
        tasks_with_due_dates = (
            self.session.query(Task).filter(Task.due_date.isnot(None)).all()
        )
        for task in tasks_with_due_dates:
            task.due_date = None
        self.session.commit()

    def get_overdue_tasks(self, current_date):
        overdue_tasks = (
            self.session.query(Task.task_id).filter(Task.due_date < current_date).all()
        )
        return [task_id for task_id, in overdue_tasks]

    def get_upcoming_tasks(self, current_date, days_ahead):
        upcoming_tasks = (
            self.session.query(Task)
            .filter(
                Task.due_date > current_date,
                Task.due_date <= current_date + timedelta(days=days_ahead),
            )
            .all()
        )
        return {task.task_id: task.due_date for task in upcoming_tasks}

# Testing code
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from models import Base

    engine = create_engine("sqlite:///taskmanager.db")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create an instance of DueDateManager
    due_date_manager = DueDateManager(session)

    # Test set_due_date method
    due_date_manager.set_due_date(task_id=1, due_date=datetime(2023, 12, 31))
    print("Due date set for task_id 1")

    # Test get_due_date method
    due_date = due_date_manager.get_due_date(task_id=1)
    print(f"Due date for task_id 1: {due_date}")

    # # Test remove_due_date method
    # due_date_manager.remove_due_date(task_id=1)
    # print("Due date removed for task_id 1")

    # # Test clear_all_due_dates method
    # due_date_manager.clear_all_due_dates()
    # print("All due dates cleared")

    # Test get_overdue_tasks method
    current_date = datetime(2023, 12, 15)
    overdue_tasks = due_date_manager.get_overdue_tasks(current_date)
    print(f"Overdue tasks: {overdue_tasks}")

    # Test get_upcoming_tasks method
    days_ahead = 7
    upcoming_tasks = due_date_manager.get_upcoming_tasks(current_date, days_ahead)
    print(f"Upcoming tasks: {upcoming_tasks}")
