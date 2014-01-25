import bottle
import os
 
@bottle.route('/')
def index():
    return "Hello World"

bottle.run(host = '0.0.0.0', port=os.environ.get('PORT', 5000))
