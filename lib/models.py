from datetime import datetime
from sqlalchemy import create_engine, desc
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///taskmanager.db")

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username='{self.username}')>"


class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String)
    priority = Column(String)
    due_date = Column(String)

    def __repr__(self):
        return (
            f"<Task(task_id={self.task_id}, user_id={self.user_id}, "
            f"title='{self.title}', description='{self.description}', "
            f"status='{self.status}', priority='{self.priority}', "
            f"due_date='{self.due_date}')>"
        )

