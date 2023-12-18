# Task Management Application

Task Management CLI application is a group project by Anita Class, aimed at providing a streamlined solution for task organization and enhanced productivity. This application offers a user-friendly interface for managing tasks effortlessly. Key features include task creation, categorization, and the assignment of priorities and due dates. Users can log in and utilize a variety of commands for tasks such as creating, updating, and viewing.

## Table of Contents

- [About](#about)
- [Commands](#commands)
  - [User Management](#user-management)
  - [Due Date Management](#due-date-management)
  - [Priority Management](#priority-management)
  - [Database Handling](#database-handling)
- [Setup](#setup)
- [Usage Examples](#usage-examples)
- [License](#license)
- [Contact](#contact)

## About

This CLI application provides functionality for managing tasks, including user registration, login, setting due dates, managing priorities, and more.
It aslo features:

- Create, read, update, and delete tasks.
- Categorize tasks and assign priorities and due dates.
- User authentication for personalized task management.


## Commands

### User Management

- `signup(username, password)`: Method for user registration.
- `login(username, password)`: Method for user login.

### Due Date Management

- `set_due_date(task_id, due_date)`: Set a due date for a task.
- `get_due_date(task_id)`: Retrieve the due date for a task.
- `remove_due_date(task_id)`: Remove the due date for a task.
- `clear_all_due_dates()`: Remove due dates for all tasks.

### Priority Management

- `set_task_priority(task_id, priority)`: Set the priority for a task.
- `get_task_priority(task_id)`: Retrieve the priority for a task.
- `remove_task(task_id)`: Remove a task from the database.
- `get_highest_priority_task()`: Retrieve the task with the highest priority.

### Database Handling

- `create_task(user_id, title, description, status, priority, due_date)`: Create a new task in the database.
- `read_tasks(user_id)`: Retrieve tasks for a specific user from the database.
- `update_task(task_id, **kwargs)`: Update a task in the database.
- `delete_task(task_id)`: Delete a task from the database.

## Setup

1. Clone the repository to your local machine.
2. Install the necessary dependencies by running `pip install -r requirements.txt`.
3. Initialize the database by running `python init_db.py`.
4. Run the CLI application using `python cli_app.py`.

## Usage Examples

Here are some examples of how to use the CLI commands:

```bash
# User signup
python cli_app.py signup <username> <password>

# Set due date for a task
python cli_app.py set_due_date <task_id> <due_date>

# Get the due date for a task
python cli_app.py get_due_date <task_id>

# ...

