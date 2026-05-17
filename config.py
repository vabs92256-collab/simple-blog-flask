import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'professional-secret-key-123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False