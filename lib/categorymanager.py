from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Task, Category, task_category_association, Base


class CategoryManager:
    def __init__(self, db_session):
        self.db_session = db_session

    def create_category(self, user_id, name):
        category = Category(user_id=user_id, name=name)
        self.db_session.add(category)
        self.db_session.commit()
        return category

    def assign_task_to_categories(self, task_id, category_ids):
        task = self.db_session.query(Task).filter_by(task_id=task_id).first()
        categories = (
            self.db_session.query(Category)
            .filter(Category.category_id.in_(category_ids))
            .all()
        )

        if task and categories:
            task.categories.extend(categories)
            self.db_session.commit()
            return task


if __name__ == "__main__":
    engine = create_engine("sqlite:///taskmanager.db")
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    category_manager = CategoryManager(session)

    # Create users
    user1 = User(username="user161", password_hash="password161")
    session.add(user1)
    session.commit()

    # Create tasks
    task1 = Task(user_id=user1.user_id, title="Task 1cvb")
    task2 = Task(user_id=user1.user_id, title="Task 2efr")
    task3 = Task(user_id=user1.user_id, title="Task 2fgr")
    task4 = Task(user_id=user1.user_id, title="Task 2gva")
    task5 = Task(user_id=user1.user_id, title="Task 2ere")
    task6 = Task(user_id=user1.user_id, title="Task 2fa2")
    task7 = Task(user_id=user1.user_id, title="Task 233a")
    task8 = Task(user_id=user1.user_id, title="Tasker")
    session.add_all([task1, task2, task3, task4, task5, task6, task6, task8])
    session.commit()

    # Create categories
    category1 = category_manager.create_category(
        user_id=user1.user_id, name="Category A"
    )
    category2 = category_manager.create_category(
        user_id=user1.user_id, name="Category B"
    )

    # Assign tasks to multiple categories
    category_manager.assign_task_to_categories(
        task_id=task1.task_id,
        category_ids=[category1.category_id, category2.category_id],
    )
    category_manager.assign_task_to_categories(
        task_id=task2.task_id, category_ids=[category2.category_id]
    )

    # Print user, tasks, and categories with their relationships
    print("User:")
    print(user1)

    print("\nTasks:")
    for task in user1.tasks:
        print(task)

    print("\nCategories:")
    for category in user1.categories:
        print(category)
        for task in category.tasks:
            print(f"  - {task}")
