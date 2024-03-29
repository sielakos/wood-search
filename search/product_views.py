# -*- coding: utf-8 -*-
from app import app
from database import db
from flask import render_template, request, json, redirect, url_for
from bson.objectid import ObjectId
from filters import replace_nl
from auth import has_role_decorator, is_owner_decorator


@app.route('/products/')
def show_products():
    products = db.Product.find()
    return render_template('product/show_products.html', products=products)


@app.route('/products/json', methods=['POST', 'GET'])
@has_role_decorator('ROLE_ADMIN')
def get_products():
    products = db.Product.find()
    products_json = []
    for product in products:
        product_dict = product.to_dict()
        products_json.append(product_dict)

    return json.dumps(products_json)


def add_product_from_data(data):
    product = db.Product()
    product.name = replace_nl(data['name'], put_in='')
    product.price = float(data['price'])
    product.description = replace_nl(data['description'])
    product.company_id = ObjectId(data['company']['_id'])
    product.validate()
    product.save()
    return product


def add_product_to_company(product):
    company = db.Company.find_one_or_404({'_id': product.company_id})
    company.products_ids.append(product['_id'])
    company.save()


@app.route('/products/add', methods=['GET', 'POST'])
@has_role_decorator('ROLE_ADMIN')
def add_product():
    if request.method == 'POST':
        data = request.get_json(force=True)
        product = add_product_from_data(data)
        add_product_to_company(product)
        return "OK"

    companies = db.Company.find()
    return render_template('product/add_product.html', companies=companies)


def remove_product_from_company(product):
    company = product.company
    if company is not None and product['_id'] in company.products_ids:
        company.products_ids.remove(product['_id'])
        company.save()


@app.route('/products/edit/<product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = db.Product.find_one_or_404({'_id': ObjectId(product_id)})

    @is_owner_decorator(product.company['_id'])
    def action():
        if request.method == 'POST':
            data = request.get_json(force=True)
            product.name = replace_nl(data['name'], put_in='')
            product.price = float(data['price'])
            product.description = replace_nl(data['description'])

            if product.company is None or str(product.company_id) != data['company']['_id']:
                remove_product_from_company(product)
                product.company_id = ObjectId(data['company']['_id'])
                add_product_to_company(product)

            product.save()
            return 'OK'

        companies = db.Company.find()

        return render_template('product/edit_product.html', product=product, companies=companies)

    return action()


@app.route('/products/remove/<product_id>', methods=['GET', 'POST'])
def remove_product(product_id):
    product = db.Product.find_one_or_404({'_id': ObjectId(product_id)})

    @is_owner_decorator(product.company['_id'])
    def action():
        remove_product_from_company(product)
        product.delete()
        return redirect(url_for('show_products'))

    return action()