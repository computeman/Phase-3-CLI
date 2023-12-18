from sqlalchemy.orm import sessionmaker


class CategoryManager:
    def _init_(self, db_session):
        self.db_session = db_session

    def create_category(self, user_id, name):
        # Create a new category for a specific user
        category = Category(
            user_id=user_id, name=name
        )  # Assuming Category is already defined in your model
        self.db_session.add(category)
        self.db_session.commit()
        return category

    def assign_task_to_category(self, task_id, category_id):
        # Link a task to a specific category
        task = self.db_session.query(Task).filter_by(task_id=task_id).first()
        category = (
            self.db_session.query(Category).filter_by(category_id=category_id).first()
        )

        if task and category:
            task.categories.append(category)
            self.db_session.commit()
            return task


# Example usage:
if _name_ == "_main_":
    from sqlalchemy import create_engine
    from models import Category, Task  # Import your actual model classes
    from models import Base  # Import your actual declarative base

    engine = create_engine("sqlite:///taskmanager.db")
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create an instance of CategoryManager
    category_manager = CategoryManager(session)

    # Example: Create a category
    user_id = 1  # Replace with the actual user ID
    category_name = "Work"
    new_category = category_manager.create_category(user_id, category_name)
    print(f"Created category: {new_category}")

    # Example: Assign a task to a category
    task_id = 1  # Replace with the actual task ID
    category_id = 1  # Replace with the actual category ID
    task_with_category = category_manager.assign_task_to_category(task_id, category_id)
    print(f"Assigned task to category: {task_with_category}")