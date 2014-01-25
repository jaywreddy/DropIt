from bottle import run, route, request
import os
import insert
import retrieve

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
    drop = request.query.drop
    insert.addDrop(drop)

@route('/getDrops')
def getDrops():
    lng = request.query.lng
    lat = request.query.lat
    num = int(request.query.num)
    dropslist=retrieve.retrieve(lng, lat, num)
    return str(dropslist)

run(host = '0.0.0.0', port=os.environ.get('PORT', 5000))
