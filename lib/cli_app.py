#!/usr/bin/env python3


import click
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user_manager import UserManager
from duedatemanager import DueDateManager
from prioritymanager import SQLAlchemyPriorityManager
from databasehandler import DatabaseHandler
from datetime import datetime, timedelta
from models import Base, Task
from categorymanager import CategoryManager

DATABASE_URL = "sqlite:///taskmanager.db"


@click.group()
def cli():
    pass


# UserManager Commands
@cli.command()
@click.argument("username")
@click.argument("password")
def signup(username, password):
    user_manager = UserManager(DATABASE_URL)
    user_manager.signup(username, password)


@cli.command()
@click.argument("username")
@click.argument("password")
def login(username, password):
    user_manager = UserManager(DATABASE_URL)
    user_manager.login(username, password)


# DueDateManager Commands
@cli.command()
@click.argument("task_id", type=int)
@click.argument("due_date", type=click.DateTime(formats=["%Y-%m-%d"]))
def set_due_date(task_id, due_date):
    due_date_manager = DueDateManager(DATABASE_URL)
    due_date_manager.set_due_date(task_id, due_date)


@cli.command()
@click.argument("task_id", type=int)
def get_due_date(task_id):
    due_date_manager = DueDateManager(DATABASE_URL)
    due_date = due_date_manager.get_due_date(task_id)
    click.echo(f"Due date for task_id {task_id}: {due_date}")


@cli.command()
@click.argument("task_id", type=int)
def remove_due_date(task_id):
    due_date_manager = DueDateManager(DATABASE_URL)
    due_date_manager.remove_due_date(task_id)


@cli.command()
def clear_all_due_dates():
    due_date_manager = DueDateManager(DATABASE_URL)
    due_date_manager.clear_all_due_dates()


@cli.command()
@click.argument("task_id", type=int)
@click.argument("priority")
def set_task_priority(task_id, priority):
    priority_manager = SQLAlchemyPriorityManager(DATABASE_URL)
    priority_manager.set_task_priority(task_id, priority)


# SQLAlchemyPriorityManager Commands
@cli.command()
@click.argument("task_id", type=int)
def get_task_priority(task_id):
    priority_manager = SQLAlchemyPriorityManager(DATABASE_URL)
    priority = priority_manager.get_task_priority(task_id)
    click.echo(f"Priority for task_id {task_id}: {priority}")


@cli.command()
@click.argument("task_id", type=int)
def remove_task(task_id):
    priority_manager = SQLAlchemyPriorityManager(DATABASE_URL)
    priority_manager.remove_task(task_id)


@cli.command()
def get_highest_priority_task():
    priority_manager = SQLAlchemyPriorityManager(DATABASE_URL)
    highest_priority_task = priority_manager.get_highest_priority_task()
    click.echo(f"Highest priority task: {highest_priority_task}")


# DatabaseHandler Commands
@cli.command()
@click.argument("user_id", type=int)
@click.argument("title")
@click.argument("description")
@click.argument("status")
@click.argument("priority")
@click.argument("due_date", type=click.DateTime(formats=["%Y-%m-%d"]))
def create_task(user_id, title, description, status, priority, due_date):
    database_handler = DatabaseHandler(DATABASE_URL)
    database_handler.create_task(
        user_id, title, description, status, priority, due_date
    )


@cli.command()
@click.argument("user_id", type=int)
def read_tasks(user_id):
    database_handler = DatabaseHandler(DATABASE_URL)
    tasks = database_handler.read_tasks(user_id)
    click.echo("Tasks:")
    for task in tasks:
        click.echo(task)


@cli.command()
@click.argument("task_id", type=int)
@click.option("--status", required=True, help="New status for the task")
def update_task(task_id, status):
    database_handler = DatabaseHandler(DATABASE_URL)
    database_handler.update_task(task_id, status=status)


@cli.command()
@click.argument("task_id", type=int)
def delete_task(task_id):
    database_handler = DatabaseHandler(DATABASE_URL)
    database_handler.delete_task(task_id)


# CategoryManager Commands
@cli.command()
@click.argument("user_id", type=int)
@click.argument("name")
def create_category(user_id, name):
    category_manager = CategoryManager(DATABASE_URL)
    category_manager.create_category(user_id, name)


@cli.command()
@click.argument("task_id", type=int)
@click.argument("category_ids", type=int, nargs=-1)
def assign_task_to_categories(task_id, category_ids):
    category_manager = CategoryManager(DATABASE_URL)
    category_manager.assign_task_to_categories(task_id, category_ids)


if __name__ == "__main__":
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Pass the session to DueDateManager
    due_date_manager = DueDateManager(session)
    cli()
