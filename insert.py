from pymongo import Connection, MongoClient, GEO2D


#to be specified
mongoURL="mongodb://dropit:droppers123@ds027779.mongolab.com:27779/dropit"
conn = Connection(mongoURL)
db = conn.dropit
drops = db.drops
raw = db.raw
users = db.users
def setup():
    drops.create_index([('loc',GEO2D)])

def insert(drop):
    
    raw.insert(drop)
    drops.insert(strip(drop))    


def strip(drop):
    return drop
	
