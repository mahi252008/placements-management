import os

class Config:
    SECRET_KEY = "mysecretkey"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:mp@localhost/itmdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
