#! /usr/bin/env python3
# coding: utf-8

import os,json
from flask import Flask,render_template

app=Flask(__name__)
app.config.update({
    'SECRET_KEY':'a random string'
    })

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

@app.route('/')
def index():
    with open('/home/shiyanlou/files/helloshiyanlou.json','r') as f:
        cont_1=json.loads(f.read())
    with open('/home/shiyanlou/files/helloworld.json','r') as fl:
        cont_2=json.loads(fl.read())
    return render_template('file.html',cont_1=cont_1,cont_2=cont_2)

@app.route('/files/<filename>')
def file(filename):
#    if os.path.exist('/home/shiyanlou/files/filename.json') is not True:
#        return redirect(url_for('not_found'))
#    if filename == 'helloshiyanlou':
    with open('/home/shiyanlou/files/helloshiyanlou.json','r') as fk:
        content=json.loads(fk.read())
#    elif filename == 'helloworld':
#        with open('/home/shiyanlou/files/helloworld.json','r') as fh:
#            content=json.loads(fh.read())

    return render_template('index.html',content=content)

if __name__=='__main__':
    app.run()

