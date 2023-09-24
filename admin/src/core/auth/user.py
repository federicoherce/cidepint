from sqlalchemy import Column, Integer, String
from src.core.database import database as db
from datetime import datetime



class Users(db.Model):
    __tablename__ = "users"  # Nombre de la tabla
    id = db.Column(db.Integer, primary_key=True, unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    inserted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self,email =None, password=None):
        self.email = email
        self.password = password
        
