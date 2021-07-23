from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from app import db

categori_blog = Table('category_blog', db.metadata,
                      Column('id_category', Integer, ForeignKey(
                          'blog.id', ondelete='cascade')),
                      Column('id_blog', Integer, ForeignKey(
                          'category.id', ondelete='cascade'))
                      )


class Category(db.Model):
    __tanlename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    description = Column(String(256), nullable=True, unique=False)
    slung = Column(String(128), nullable=False, unique=True)
    blog = db.relationship("Blog", secondary=categori_blog,
                           back_populates="category")


class Blog(db.Model):
    __tanlename__ = 'blog'
    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False, unique=True)
    summery = Column(String(256), nullable=True, unique=False)
    content = Column(Text, nullable=False, unique=True)
    slug = Column(String(128), nullable=False, unique=True)
    category = db.relationship(
        'Category', secondary=categori_blog, back_populates='blog')
