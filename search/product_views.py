# -*- coding: utf-8 -*-
from app import app
from database import db
from flask import render_template, redirect, url_for, request, json
from bson.objectid import ObjectId

def get_products_from_cursor(products_cursor):
    products = []

    for product in products_cursor:
        product.company = db.Company.get_from_id(product.company_id)
        products.append(product)

    return products

@app.route('/show_products')
def show_products():
    products = get_products_from_cursor(db.Product.find())

    return render_template('show_products.html', products=products)


def add_product_from_data(data):
    product = db.Product()
    product.name = data['name']
    product.price = float(data['price'])
    product.description = data['description']
    product.company_id = ObjectId(data['company']['_id'])
    product.validate()
    product.save()
    return product


def add_product_to_company(product):
    company = db.Company.find_one_or_404({'_id': product.company_id})
    company.products_ids.append(product['_id'])
    company.save()


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        data = request.get_json(force=True)
        product = add_product_from_data(data)
        add_product_to_company(product)
        return "OK"

    companies = db.Company.find()
    return render_template('add_product.html', companies=companies)