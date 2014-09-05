# -*- coding: utf-8 -*-
from flask import redirect, url_for
from app import app
import product_views
import companies_views
import login
import user_views

@app.route('/')
def index():
    return redirect(url_for('show_products'))


