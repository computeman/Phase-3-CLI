# db/user_manager.py
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from db.models import User
from sqlalchemy import create_engine
import bcrypt

class UserManager:
    def __init__(self, db_url='sqlite:///taskmanager.db'):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def signup(self, username, password):
        hashed_password = self._hash_password(password)
        user = User(username=username, password=hashed_password)

        session = self.Session()
        try:
            session.add(user)
            session.commit()
            return user
        except IntegrityError:
            session.rollback()
            return None
        finally:
            session.close()

    def login(self, username, password):
        user = self._get_user_by_username(username)
        if user and self._check_password(password, user.password):
            return user
        return None

    def _get_user_by_username(self, username):
        session = self.Session()
        user = session.query(User).filter_by(username=username).first()
        session.close()
        return user

    def _hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def _check_password(self, password, hashed_password):
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
