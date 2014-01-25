from pymongo import MongoClient, GEO2D


#to be specified
client = MongoClient('localhost', 27017)
db = client.dropit
drops = db.drops

def setup():
	db.drops.create_index([('loc',GEO2D)])


def insert(drop):
    drops.insert(drop)
	
