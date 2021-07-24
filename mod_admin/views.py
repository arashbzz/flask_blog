from os import error
import re
from sqlalchemy.exc import IntegrityError
from flask import session, render_template, request, abort, flash, redirect, url_for
from werkzeug.security import check_password_hash
from . import admin
from app import db
from mod_users.models import User
from mod_users.forms import Login_form
from .utils import admin_only_viwe
from mod_blog.forms import CreateBlog
from mod_blog.models import Blog
from mod_users.forms import RegisterForm


@admin.route('/')
@admin_only_viwe
def index():
    return render_template('/admin/index.html')


@admin.route('/login', methods=['POST', 'GET'])
def login():
    form = Login_form(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit:
            abort(400)
        user = User.query.filter(
            User.email.ilike(f'{form.email.data}')).first()
        if not user:
            flash('incorrect credential', 'error')
            return render_template('admin/login_template.html', form=form)
        if not user.check_password(form.password.data):

            flash('incorrect credential', 'error')
            return render_template('admin/login_template.html', form=form)
        if not user.is_user_admin():
            flash('you are not admin', 'error')
            return render_template('admin/login_template.html', form=form)
        session['email'] = user.email
        session['id'] = user.id
        session['role'] = user.role
        print(session)
        return redirect(url_for('admin.index'))
    if session.get('role') == 1:
        return redirect(url_for('admin.index'))
    return render_template('admin/login_template.html', form=form)


@admin.route('/logout')
@admin_only_viwe
def logout():
    session.clear()
    flash('you logout successfully.', 'warning')
    return redirect(url_for('admin.login'))


@admin.route('/post/new', methods=['POST', 'GET'])
@admin_only_viwe
def create_post():
    form = CreateBlog(request.form)
    if request.method == "POST":
        if not form.validate_on_submit:
            flash('insert required information')
            return render_template('admin/add_new_post.html', form=form)
        blog = Blog()
        blog.title = form.title.data
        blog.summery = form.summery.data
        blog.content = form.content.data
        blog.slug = form.slug.data

        try:
            db.session.add(blog)
            db.session.commit()
            flash('your blog submit sucsefully')
            return redirect(url_for('admin.index'))
        except IntegrityError:
            db.session.rollback()
            flash('there is a blog with this name. please change the name.')
            return render_template('admin/add_new_post.html', form=form)
    return render_template('admin/add_new_post.html', form=form)


@admin.route('/users_list')
@admin_only_viwe
def users_list():
    users = User.query.order_by(User.id.desc()).all()
    return render_template('admin/user_list.html', users=users)


@admin.route('/create_new_user', methods=['GET', 'POST'])
@admin_only_viwe
def create_new_user():

    form = RegisterForm(request.form)

    if request.method == 'POST':
        user = User()
        if not form.validate_on_submit():
            return render_template('admin/create_new_user.html', form=form)

        if form.password.data != form.confirm_password.data:
            error_message = 'password and confirm password are not match'
            form.password.errors.append(error_message)
            return render_template('admin/create_new_user.html', form=form)

        old_user = User.query.filter(User.email.ilike(form.email.data)).first()
        if old_user:
            flash('-------')
            return render_template('admin/create_new_user.html', form=form)

        user.full_name = form.full_name.data
        user.email = form.email.data
        user.set_password(str(form.password.data))

        try:
            db.session.add(user)
            db.session.commit()
            flash('you create your account sucssesfully')
        except IntegrityError:
            db.session.rollback()
            flash('email is inused')

    return render_template('admin/create_new_user.html', form=form)


@admin.route('/admin/list_post')
@admin_only_viwe
def post_list():
    posts = Blog.query.all()
    return render_template('admin/post_list.html',posts = posts)

@admin.route('/admin/single_post/<string:slug>')
@admin_only_viwe
def single_post_viewing(slug):
    post =Blog.query.filter(Blog.slug == slug).first_or_404()
    return post.content

@admin.route('/delete_post/<int:id>')
@admin_only_viwe
def delete_post(id):
    post = Blog.query.filter(Blog.id == id).first_or_404()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('admin.post_list'))