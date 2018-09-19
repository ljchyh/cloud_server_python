#coding=utf-8
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

import flask
from flask import Flask,jsonify
import json
import MySQLdb
import datetime


conn = MySQLdb.connect(
        host='localhost',
        port = 3306,
        user = 'root',
        passwd = '19920527',
        db = 'test',
        )


#cur = conn.cursor()
#建表，仅执行一次.
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
#插入数据
#cur.execute("insert into student values('2','Tom','3 year 2 class','9')")
#寻找指定数据并更新
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")
#cur.close()
#conn.commit()
#conn.close()


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World112!"

@app.route("/upload_img", methods=['GET', 'POST'])
def upload_img():
    if flask.request.method == 'GET':
        return 'waiting for img'
    else:        
        timenow = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file = flask.request.files["file"]
        if file:
            print 'upload img OK'
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
