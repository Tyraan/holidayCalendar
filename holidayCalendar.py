#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Tyraan Tao ,2017/4/7
# tyraan@qq.com
import os,sqlite3,json
from flask import Flask,request,session,g,url_for,render_template,jsonify
app  = Flask(__name__)
app.config.from_object('config')
def connect_db():
    """Connects to the specific database."""

    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('dota2.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """open a new database connection if none yet for the current application
    contex"""
    if not hasattr(g,'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.before_request
def before_request():
    g.db = connect_db()
################################
#route
@app.route('/')
def index():
    cur = g.db.execute('select id,currentNumber,date from DOTA2 order by id desc')
    datas = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('index.html',datas = datas)
################################

if __name__ =='__main__':
    app.run()

