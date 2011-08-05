#!/usr/bin/env python
#
# (c) 2011 Joseph Adams


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from func import *
from models import *


class DumperHandler(webapp.RequestHandler):
    def get(self):
        data = []
        
        q = Thing.all().fetch(9999)
        
        for thing in q:
            data.append(thing.title)
            data.append(thing.author)
            data.append(thing.isbn)
            data.append(thing.thingid)
            
        self.response.out.write(data) 
        
        
def main():
    application = webapp.WSGIApplication([
      ('/datadumper', DumperHandler)
      ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
