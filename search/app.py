# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

app.config.update(
    {
        'MONGODB_DATABASE': 'test004',
        'DEBUG': True,
    }
)

app.config.from_envvar('SEARCH_SETTINGS', silent=True)