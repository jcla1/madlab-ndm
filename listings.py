#!/usr/bin/env python
#
# (c) 2011 Joseph Adams


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import users

from models import *
from func import *

class ListingHandler(webapp.RequestHandler):
    def get(self):
      q = Thing.all().fetch(9999)
      for thing in q:
          self.response.out.write(thing.title)
          self.response.out.write("<br />")

def main():
    application = webapp.WSGIApplication([
      ('/listofbooks', ListingHandler)
      ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
