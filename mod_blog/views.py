from . import blog
from flask import render_template
from .models import Blog

@blog.route('/')
def index():
    blogs = Blog.query.all()
    return render_template('blog/index.html' , blogs = blogs )

@blog.route('/<string:slug>')
def single_blog (slug):
    post= Blog.query.filter(Blog.slug == slug).first_or_404()
    return post.title