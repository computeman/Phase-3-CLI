import sys
from pytermgui import *

# Import UserManager from the correct path
from user_manager import UserManager

# Create an instance of UserManager
user_manager = UserManager()


# Define the signup command
def signup_command(button):
    username = InputField("Enter username:")
    password = InputField("Enter password:")

    # Access the input directly (replace 'input_attribute' with the actual attribute name)
    username_text = username.input_attribute
    password_text = password.input_attribute

    user = user_manager.signup(username_text, password_text)
    if user:
        window.success(f"User {user.username} signed up successfully!")
    else:
        window.error(f"User with username {username_text} already exists.")


# Define the login command
def login_command(button):
    username = InputField("Enter username:")
    password = InputField("Enter password:")
    user = user_manager.login(username, password)
    if user:
        window.success(f"User {user.username} logged in successfully!")
    else:
        window.error(f"Login failed for user {username}.")


# Create a window with buttons for Signup and Login commands
with WindowManager() as manager:
    window = Window("[wm-title]User Authentication", "")
    window += Button("[72 italic]Signup", signup_command)
    window += Button("[72 italic]Login", login_command)
    window += Button("[157 bold]Exit", sys.exit)

    manager += window
    manager.run()
