from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.hybrid import hybrid_method

from . import Base, session


class User(Base):

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, nullable=False)
    created_at = Column(DateTime(), default=datetime.now)
    password = Column(String, nullable=False)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def save(self):
        session.add(self)
        session.commit()

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @hybrid_method
    def is_correct_password(self, password):
        return self.password == password

    @property
    def is_active(self):
        """Always True, as all users are active."""
        return True

    @property
    def is_anonymous(self):
        """Always False, as anonymous users aren't supported."""
        return False

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        """Requires use of Python 3"""
        return str(self.id)
