# -*- coding: utf-8 -*-
from search.app import app
import search.database
import search.models
import search.views
import search.filters
import search.auth

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)