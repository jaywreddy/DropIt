from pymongo import MongoClient


#to be specified
client = MongoClient('localhost', 27017)
db = client.dropit
drops = db.drops

def retrieve(lng, lat, number):


    dropsitr = drops.find({"loc": {"$near":[lng,lat]}}).limit(number)
    dropslist=list(dropsitr)

    return dropslist
