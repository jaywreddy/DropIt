import bottle
import os
 
@bottle.route('/')
def index():
    return "Hello World"

bottle.run() 
