from flask import Blueprint, render_template
import pymysql
import socket

app_route = Blueprint('first_route', __name__)

@app_route.route('/key')
def key():
    connect = pymysql.connect(host='mysql', user='user', password='password',
            db='mydb', charset='utf8')
    cursor = connect.cursor()
    return(str(socket.gethostbyname(socket.gethostname())))

@app_route.route('/image')
def image():
    return "by"
