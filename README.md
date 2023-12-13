# Task Management Application

Task Management CLI application is a group project by Anita Class, aimed at providing a streamlined solution for task organization and enhanced productivity. This application offers a user-friendly interface for managing tasks effortlessly. Key features include task creation, categorization, and the assignment of priorities and due dates. Users can log in and utilize a variety of commands for tasks such as creating, updating, and viewing.

## Features

- Create, read, update, and delete tasks.
- Categorize tasks and assign priorities and due dates.
- User authentication for personalized task management.

## Database Design and Setup

### Database Models

- **User Model:**
  - Attributes: `user_id, username, password_hash`
- **Task Model:**
  - Attributes: `task_id, user_id, title, description, status, priority, due_date`
- **Category Model:**
  - Attributes: `category_id, user_id, name`

### Alembic Migrations

- Create migrations for creating the Users, Tasks, and Categories tables.

### Relationships

- **User-Task Relationship:** One-to-Many (User has many Tasks)
- **User-Category Relationship:** One-to-Many (User has many Categories)
- **Task-Category Relationship:** Many-to-Many (Task can belong to multiple Categories, Category can have multiple Tasks)

### Seeding Data

Seed the database with initial data.

## User Creation and Authentication (Kelvin)

### UserManager Class

- `signup(username, password)`: Create a new user and store in the database.
- `login(username, password)`: Verify user credentials and return user details.

## Task and Category Management (Branham)

### TaskManager Class

- `create_task(user_id, title, description)`: Create a new task for a specific user.
- `view_tasks(user_id)`: Retrieve and display all tasks for a specific user.
- `update_task_status(task_id, status)`: Update the status of a task.

### CategoryManager Class

- `create_category(user_id, name)`: Create a new category for a specific user.
- `assign_task_to_category(task_id, category_id)`: Link a task to a specific category.

## Priority and Due Date Management (Felix)

### PriorityManager Class

- `set_task_priority(task_id, priority)`: Assign a priority level to a task.

### DueDateManager Class

- `set_due_date(task_id, due_date)`: Define a due date for a task.

## CLI Commands and Click Integration

Commands to be divided among collaborators as GitHub issues.

## Considerations

1. **Package Structure:**
   - Organize the project into packages such as `models`, and `cli`.
   - Separate database models, manager classes, and CLI commands into different modules.

2. **Pipenv and Virtual Environment:**
   - Use Pipenv to manage dependencies and create a well-maintained virtual environment.

3. **Testing:**
   - Write unit tests for each method in the manager classes.
   - Consider using testing frameworks to automate and streamline the testing process.

4. **Documentation:**
   - Provide detailed documentation for each class and method, including their purpose and usage.
   - Include instructions for running migrations, starting the application, and using the CLI.

5. **Version Control:**
   - Use version control (Git) to track changes and collaborate effectively within the team.

