from pymongo import MongoClient


#to be specified
mongoURL="mongodb://dropit:droppers123@ds027779.mongolab.com:27779/dropit"
client = MongoClient(mongoURL)
db = client.dropit
drops = db.drops
users= db.user_info
def retrieve(user_id):
   #{"comment": drop.status, "drop":db.drops.find({"drop_id":drop.drop_id})}  
    drop_ids = users.find_one({"user_id":user_id})['drops']
    dropslist = []
    for drop_id in drop_ids:
	drop = drops.find_one({"_id":drop_id['drop']})
        drop["status"]=drop_id["status"]
        dropslist.append(drop)
    return dropslist
