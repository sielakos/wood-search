# -*- coding: utf-8 -*-
from search.app import app
from search.database import db
from flask import session, redirect, url_for, render_template
from functools import wraps
from search.hashing import get_salt, hash_password


def create_default_user():
    if db.User.find().count() == 0:
        user = db.User()
        user.name = 'admin'
        user.salt = get_salt()
        user.pass_hash = hash_password('password', user.salt)
        user.email = 'sielakos@gmail.com'
        user.roles = ['ROLE_ADMIN']
        user.save()


@app.route('/login', methods=['GET', 'POST'])
def login():
    create_default_user()

    error = None

    return render_template('login.html', error=error)