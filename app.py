from bottle import run, route, request
import os

 
@route('/')
def index():
    return "Hello World"

@route('/login')
def login():
    username = request.query.username
    password = request.query.password 
    return "u:"+username+" , p:"+password

@route('/addDrop')
def addDrop():
    return ":"

@route('/getDrops')
def getDrops():
    return "d"


run(host = '0.0.0.0', port=os.environ.get('PORT', 5000))
