from pymongo import MongoClient


#to be specified
mongoURL="mongodb://dropit:droppers123@ds027779.mongolab.com:27779/dropit"
client = MongoClient(mongoURL)
db = client.dropit
drops = db.drops

def retrieve(user_id):
     
    dropsitr= [{"status": drop.status, "drop":db.drops.find({"drop_id":drop.drop_id})} for drop in db.users.user_id.drops]
	
    
   # dropsitr = drops.find({"loc": {"$near":[lng,lat]}}).limit(number)
    dropslist=list(dropsitr)

    return dropslist
