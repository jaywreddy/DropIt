from pymongo import Connection, MongoClient, GEO2D


#to be specified
mongoURL="mongodb://dropit:droppers123@ds027779.mongolab.com:27779/dropit"
conn = Connection(mongoURL)
db = conn.dropit
drops = db.drops

users = db.user_info
def setup():
    drops.create_index([('loc',GEO2D)])

def addDrop(lat, lng, comment, picture, video, recipients, sender):
    
    drop_id = drops.insert({"comment":comment, "loc":[lng, lat],"picture":picture, "sender":sender})
    print(drop_id)

    for user_id in recipients:
        users.update({"user_id":user_id}, {"$addToSet": {"drops": {"drop":drop_id, "status":0}}}, upsert=True)
        #notify users

def read_drop(user_id, drop_id):
    users.update({"user_id":user_id}, {"$": {"drops": {"drop": drop_id, "status":1}}}, upsert=True)	
    
def register_user_device(user_id, device_id):
    users.update({"user_id":user_id},{ "device_id":device_id})
    
def strip(drop):
    return drop
	
