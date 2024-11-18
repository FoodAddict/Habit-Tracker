import os

class Config:
    SECRET_KEY = os.urandom(24)  # Generate a random secret key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Using SQLite for simplicity
    SQLALCHEMY_TRACK_MODIFICATIONS = False

