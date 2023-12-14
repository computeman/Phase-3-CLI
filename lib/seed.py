from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Task, Category, task_category_association

# Set up the SQLite database engine
engine = create_engine("sqlite:///taskmanager.db")

# Bind the engine to the Base class
Base.metadata.bind = engine

# Create a session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create a Faker instance
fake = Faker()

# Create users
users = []
for _ in range(5):
    user = User(username=fake.user_name(), password_hash=fake.sha256())
    users.append(user)

session.add_all(users)
session.commit()

# Create tasks and categories
for user in users:
    for _ in range(10):
        task = Task(
            user_id=user.user_id,
            title=fake.sentence(),
            description=fake.paragraph(),
            status=fake.random_element(elements=("Open", "In Progress", "Completed")),
            priority=fake.random_element(elements=("High", "Medium", "Low")),
            due_date=fake.date_this_year(),
        )
        session.add(task)

        category = Category(user_id=user.user_id, name=fake.word())
        session.add(category)

        task.categories.append(category)

session.commit()

print("Seeding complete.")
