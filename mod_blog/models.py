from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from app import db




class Category(db.Model):
    __tanlename__= 'category'
    id =Column(Integer, primary_key=True)
    name =Column(String(128),nullable= False, unique=True)
    description = Column(String(256),nullable=True, unique= False)
    slung =Column(String(128), nullable=False, unique= True)

class Blog(db.Model):
    __tanlename__= 'blog'
    id =Column(Integer, primary_key=True)
    name =Column(String(128),nullable= False, unique=True)
    description = Column(String(256),nullable=True, unique= False)
    content= Column(Text, nullable= False, unique=True)
    slung =Column(String(128), nullable=False, unique= True)