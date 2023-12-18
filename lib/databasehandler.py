import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Task, Category


class DatabaseHandler:
    def __init__(self, database_url="sqlite:///taskmanager.db"):
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def create_task(self, user_id, title, description, status, priority, due_date):
        session = self.Session()
        task = Task(
            user_id=user_id,
            title=title,
            description=description,
            status=status,
            priority=priority,
            due_date=due_date,
        )
        session.add(task)
        session.commit()
        session.close()

    def read_tasks(self, user_id):
        session = self.Session()
        tasks = session.query(Task).filter_by(user_id=user_id).all()
        session.close()
        return tasks

    def update_task(self, task_id, **kwargs):
        session = self.Session()
        task = session.query(Task).filter_by(task_id=task_id).first()
        if task:
            for key, value in kwargs.items():
                setattr(task, key, value)
            session.commit()
        session.close()

    def delete_task(self, task_id):
        session = self.Session()
        task = session.query(Task).filter_by(task_id=task_id).first()
        if task:
            session.delete(task)
            session.commit()
        session.close()
