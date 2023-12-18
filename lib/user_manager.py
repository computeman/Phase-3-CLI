# db/user_manager.py
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from models import User, Task, Category, Base, task_category_association
from sqlalchemy import create_engine
import bcrypt


class UserManager:
    def __init__(self, db_url="sqlite:///taskmanager.db"):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def signup(self, username, password):
        hashed_password = self._hash_password(password)
        user = User(username=username, password_hash=hashed_password)

        session = self.Session()
        try:
            session.add(user)
            session.commit()
            print(f"User added: {user.username}")  # Print statement
            return user
        except IntegrityError:
            session.rollback()
            print(f"User with username {username} already exists.")  # Print statement
            return None
        finally:
            session.close()

    def login(self, username, password):
        user = self._get_user_by_username(username)
        if user and self._check_password(password, user.password_hash):
            print(f"User logged in: {user.username}")  # Print statement
            return user
        print(f"Login failed for user: {username}")  # Print statement
        return None

    def _get_user_by_username(self, username):
        session = self.Session()
        user = session.query(User).filter_by(username=username).first()
        session.close()
        return user

    def _hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password

    def _check_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)

    # Define a due date for a task
    def set_due_date(self, task_id, due_date):
        task = self.session.query(Task).filter_by(task_id=task_id).first()
        if task:
            task.due_date = due_date
            self.session.commit()


# Example usage
if __name__ == "__main__":
    user_manager = UserManager()

    # Example: Sign up a user
    signed_up_user = user_manager.signup("john_doe", "password123")

    # Example: Try to sign up a user with the same username (will print a message)
    duplicate_user = user_manager.signup("john_doe", "another_password")

    # Example: Log in with correct credentials
    logged_in_user = user_manager.login("john_doe", "password123")

    # Example: Log in with incorrect credentials (will print a message)
    failed_login_user = user_manager.login("john_doe", "wrong_password")
