#!/usr/bin/env python2.7

import os
from flask import Flask,render_template,abort,redirect,url_for,request
from database import db_session as db

app=Flask(__name__)

@app.errorhandler(404)
def err404(err):
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST','PUT'])
def login():
    return 'login'

if __name__=='__main__':
    app.debug=True
    app.secret_key=os.urandom(64)
    app.run(host='127.0.0.1',port=1338)
