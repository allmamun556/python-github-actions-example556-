# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 14:37:57 2021

@author: 49157
"""

from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "Hello, world"
if __name__=="__main__":
    app.run()