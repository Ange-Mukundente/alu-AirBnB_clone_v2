#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.review import Review
from models.place import Place


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="all, delete")
    reviews = relationship("Review", backref="user", cascade="all, delete")
if __name__ == "__main__":
    from models import storage
    
    # Test create User with email, password, first_name, and last_name via the console
    user_all_attributes = User(email="a@a.com", password="pwd", first_name="fn", last_name="ln")
    storage.new(user_all_attributes)
    storage.save()
    print(f"Created User with all attributes: {user_all_attributes}")

    # Test create User with email and password via the console
    user_email_password = User(email="a@a.com", password="pwd")
    storage.new(user_email_password)
    storage.save()
    print(f"Created User with email and password: {user_email_password}")

    # List all User in MySQL (created outside the program)
    all_users = storage.all(User)
    print("All Users in MySQL:")
    for user_id, user in all_users.items():
        print(user)
