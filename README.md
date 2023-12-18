# Task Management Application

Task Management CLI application is a group project, aimed at providing a streamlined solution for task organization and enhanced productivity. This application offers a user-friendly interface for managing tasks effortlessly. Key features include task creation, categorization, and the assignment of priorities and due dates. Users can log in and utilize a variety of commands for tasks such as creating, updating, and viewing.

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

- `signup <username> <password>`: Method for user registration.
- `login <username> <password>`: Method for user login.

### Priority Management

- `set-task-priority <task_id> <priority>`: Set the priority for a task.
- `get-task-priority <task_id>`: Retrieve the priority for a task.
- `remove-task <task_id>`: Remove a task from the database.
- `get-highest-priority-task`: Retrieve the task with the highest priority.

### Category Management
- `create-category <user_id> "Category Name"`
- `assign-task-categories <task_id> <category_id1> <category_id2>`


### CRUD Handling for Tasks

- `create-task <user_id> "Title" "Description" "Status" "Priority" "2023-01-01"`: Create a new task in the database.
- `read-tasks <user_id>`: Retrieve tasks for a specific user from the database.
- `update-task <task_id> --status "New Status"`: Update a task in the database.
- `delete-task <task_id>`: Delete a task from the database.

### Due Date Management

- `set-due-date <task_id> <due_date>`: Set a due date for a task.
- `get-due-date <task_id>`: Retrieve the due date for a task.
- `remove-due-date <task_id>`: Remove the due date for a task.
- `clear-all-due-dates`: Remove due dates for all tasks.

## Setup

1. Clone the repository to your local machine.
2. Install the necessary dependencies by running `pipenv install` and `pipenv shell`.
3. Initialize the database by running `python init_db.py`.
4. Run the CLI application using `python cli_app.py` and the corresponding CLI command.


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
```

## License

MIT Licence
Copyright (c) 2023 Daudi Mwanzia

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Daudi Mwanzia - [DaudiKM - Twitter](https://twitter.com/DaudiKM) - daudimwanzia@gmail.com

Project Link: [https://github.com/computeman/Phase-3-CLI](https://github.com/computeman/Phase-3-CLI)


## Acknowledgments

The following are resources that we used.
- MDN Web Docs

