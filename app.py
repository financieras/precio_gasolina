#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hola mundo desde Flask'
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=True, port=port)