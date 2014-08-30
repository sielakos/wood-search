# -*- coding: utf-8 -*-
from app import app
from database import db
from flask import render_template, redirect, url_for, request

@app.route('/')
def index():
    return redirect(url_for('show_products'))

@app.route('/show_products')
def show_products():
    products = db.Product.find()

    for product in products:
        product.company = db.Company.get_from_id(product.company_id)

    return render_template('show_products.html', products=products)


@app.route('/show_companies')
def show_companies():
    companies = db.Company.find()
    return render_template('show_companies.html', companies=companies)


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    companies = db.Company.find()
    return render_template('add_product.html', companies=companies)


@app.route('/add_company', methods=['GET', 'POST'])
def add_company():
    if request.method == 'POST':
        company = db.Company()
        company.name = request.form['name']
        company.description = request.form['description']
        company.validate()
        company.save()
        return redirect(url_for('show_companies'))

    return render_template('add_company.html')
