from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import  Column, Integer, String
from app import db

#if role = 0 => normal user 
#if role = 1 => admin user

class User (db.Model):
    __tablename__='users'
    id = Column(Integer(), primary_key=True)
    email = Column(String(128), nullable=False, unique=True)
    password = Column(String(128), nullable=False, unique=False)
    role =Column(Integer(), nullable=False, default=0)
    full_name =Column(String(128), nullable=True, unique=False)

    def set_password(self,password):
        self.password = generate_password_hash(password)

    def check_password (self, password):
        return check_password_hash(self.password, password)
    
    def is_user_admin (self):
        return  self.role == 1