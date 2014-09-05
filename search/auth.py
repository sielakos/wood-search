# -*- coding: utf-8 -*-
from search.app import app
from search.database import db
from flask import session, redirect, url_for, request, flash
from bson.objectid import ObjectId
from functools import wraps


@app.template_global()
def get_current_user():
    user_id = session.get('user', None)

    if user_id is None:
        return None

    return db.User.fetch_one({'_id': ObjectId(user_id)})


@app.template_global()
def has_role(role, user=None):
    if user is None:
        user = get_current_user()

    return user is not None and role in user.roles


@app.template_global()
def is_owner(object_id, user=None):
    if user is None:
        user = get_current_user()

    return user is not None and (object_id in user.access_list or has_role('ROLE_ADMIN', user))


def has_role_decorator(role):
    def decorator(view):
        @wraps(view)
        def view_func(*args, **kwargs):
            if has_role(role):
                return view(*args, **kwargs)
            else:
                session['login_redirect'] = request.url
                flash('You must have role %s' % role)
                return redirect(url_for('login'))

        return view_func

    return decorator


def is_owner_decorator(object_id):
    def decorator(view):
        @wraps(view)
        def view_func(*args, **kwargs):
            if is_owner(object_id):
                return view(*args, **kwargs)
            else:
                session['login_redirect'] = request.url
                flash('You do not have access to this page')
                return redirect(url_for('login'))

        return view_func

    return decorator


def logged_in_decorator(view):
    @wraps(view)
    def view_func(*args, **kwargs):
        user = get_current_user()
        if user is not None:
            return view(*args, **kwargs)
        else:
            session['login_redirect'] = request.url
            flash('You must be logged in')
            return redirect(url_for('login'))

    return view_func
