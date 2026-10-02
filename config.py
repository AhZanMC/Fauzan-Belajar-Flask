import os

class Config:
    # Secret key untuk session & flash messages
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'punya-fauzan'
    
    # Database SQLite sederhana dulu
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False