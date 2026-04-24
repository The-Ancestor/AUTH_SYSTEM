import os
from dotenv import load_dotenv

load_dotenv() 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-key-123"
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or "jwt-dev-key"
    
    uri = os.environ.get("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_DATABASE_URI = uri or 'sqlite:///' + os.path.join(basedir, 'project.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
