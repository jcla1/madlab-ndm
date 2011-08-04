#!/usr/bin/env python
#
# (c) 2011 Joseph Adams


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template
from google.appengine.api import users

from models import *
from func import *

class NewAnnotationHandler(webapp.RequestHandler):
    def post(self):
      thingid = self.request.get("thingid")
      comment = self.request.get("comment")
      
      user = users.get_current_user()
      
      query = Thing().all().filter("thingid =", thingid)
      result = query.get()
      
      # Then add the comment to a new annotation
      a = Annotation()
      a.thing = result
      a.comment = comment
      a.creator = user
      a.put()
      
      self.redirect(THING_URL_BASE + "thing/" + thingid)
          

def main():
    application = webapp.WSGIApplication([
      ('/annotation/new', NewAnnotationHandler)
      ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
