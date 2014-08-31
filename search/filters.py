# -*- coding: utf-8 -*-
from app import app
from flask import json


@app.template_filter('jsonify')
def filter_jsonify(some_dict, **kwargs):
    if type(some_dict) == dict:
        return json.dumps(some_dict, **kwargs)

    return 'not dict!'