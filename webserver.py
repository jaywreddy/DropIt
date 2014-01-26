from bottle import post, run, route, request
import os
import insert
import retrieve

@route('/')
def index():
    return "Hello World"

@route('/login')
def login():
    device_id = request.query.device_id
    user_id = request.query.user_id
    insert.register_user_device(user_id, device_id)
    return "{status:success}"

@route('/addDrop', method="POST")
def addDrop():
    sender= request.forms.user_id
    comment = request.forms.comment #if not null
    picture = request.forms.image #if not null
    video = request.forms.video #if not null
    recipients = request.forms.recipients
    lat = request.forms.lat
    lng = request.forms.lng
    #deserialize picture

    insert.addDrop(lat, lng, comment=None, picture=None, video = None, recipients=[], sender=None)
    return "{status:success}"

@route('/getDrops')
def getDrops():
    lng = request.query.lng
    lat = request.query.lat
    user_id = request.query.user_id
    #last update
    dropslist=retrieve.retrieve(lng, lat, user_id)
    return str(dropslist)

run(host = '0.0.0.0', port=os.environ.get('PORT', 5000))
