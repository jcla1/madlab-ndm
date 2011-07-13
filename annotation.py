#!/usr/bin/env python
#
# (c) 2011 Joseph Adams


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

from models import *
from func import *

class NewAnnotationHandler(webapp.RequestHandler):
    def post(self):
      thingid = self.request.get("thingid")
      comment = self.request.get("comment")
      
      query = Thing().all().filter("thingid =", thingid)
      result = query.get()
      
      # Then add the comment to a new annotation
      a = Annotation()
      a.thing = result
      a.comment = comment
      a.put()
      
      self.response.out.write("Your annotation was added")
          

def main():
    application = webapp.WSGIApplication([
      ('/annotation/new', NewAnnotationHandler)
      ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
