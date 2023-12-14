from datetime import datetime
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import relationship
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///taskmanager.db")

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    tasks = relationship("Task", back_populates="user")
    categories = relationship("Category", back_populates="user")

    def __repr__(self):
        return f"<User(user_id={self.user_id}, username='{self.username}')>"


class Task(Base):
    __tablename__ = "tasks"
    task_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    status = Column(String)
    priority = Column(String)
    due_date = Column(String)

    user = relationship("User", back_populates="tasks")
    categories = relationship(
        "Category", secondary="task_category_association", back_populates="tasks"
    )

    def __repr__(self):
        return (
            f"<Task(task_id={self.task_id}, user_id={self.user_id}, "
            f"title='{self.title}', description='{self.description}', "
            f"status='{self.status}', priority='{self.priority}', "
            f"due_date='{self.due_date}')>"
        )


class Category(Base):
    __tablename__ = "categories"
    category_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    name = Column(String, nullable=False)


    user = relationship('User', back_populates='categories')
    tasks = relationship('Task', secondary='task_category_association', back_populates='categories')
    def __repr__(self):
        return (
            f"<Category(category_id={self.category_id}, user_id={self.user_id}, "
            f"name='{self.name}')>"
        )

# Many-to-Many association table
task_category_association = Table('task_category_association', Base.metadata,
    Column('task_id', Integer, ForeignKey('tasks.task_id')),
    Column('category_id', Integer, ForeignKey('categories.category_id'))
)



