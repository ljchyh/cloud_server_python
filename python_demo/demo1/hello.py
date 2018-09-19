#coding=utf-8
import sys
reload(sys) 
import os
sys.setdefaultencoding('utf-8')

import flask
from flask import Flask,jsonify,redirect,url_for
import json
import MySQLdb
import datetime
from werkzeug.utils import secure_filename


conn = MySQLdb.connect(
        host='localhost',
        port = 3306,
        user = 'root',
        passwd = '19920527',
        db = 'test',
        )

UPLOAD_FOLDER = '/opt/python_demo/demo1/imgs/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def insert_imgs(img,timenow):
    cursor = conn.cursor()
    cursor.execute("Insert into img(picture,time) values(%s,%s)", (MySQLdb.Binary(img),timenow))
    conn.commit()
    cursor.close()



@app.route("/")
def hello():
    return "Hello World112!"

@app.route("/upload_img", methods=['GET', 'POST'])
def upload_img():
    if flask.request.method == 'GET':
        return 'waiting for img'
    else:
        if 'file' not in flask.request.files:
            flash('No file part')
            print 'No file part'
            return 'No file part'
        timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file = flask.request.files["file"]
        if file.filename == '':
            flash('No selected file')
            print 'No selected file'
            return 'No selected file'
        if file and allowed_file(file.filename):
            print 'upload img OK'
            filename = secure_filename(file.filename)
            print 'filename ='+ filename
            #####以下两行可以把图片传到数据库，但是会让数据库变得臃肿，不建议直接放数据库
            #img = file.read()
            #insert_imgs(img,timenow)
            ######save to local path
            #file.save(file.filename)
            
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',filename=filename))
            return '上传成功' #return message to small app
        else:    
            return 'post mode 失败了'

@app.route("/user/<name>")
def user(name):
    userid = 1 
    timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cur1 = conn.cursor()
    cur1.execute("insert into user(name,time)\
            values('%s','%s')"%\
            (name,timenow))
    cur1.close()
    conn.commit()
    return "你好," + name +'\n' + timenow

@app.route("/json")
def try_json():
    t = {
        'a': 1,
        'b': 2,
        'c': [3, 4, 5]
    }
    return jsonify(t)


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='32.221.175.37', port=1111)
