#!/usr/bin/env python
#
# (c) 2011 Joseph Adams


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from func import *

class MainHandler(webapp.RequestHandler):
    def get(self):
	    self.response.out.write("This project is currently under development, sorry guys!")
      

def main():
    application = webapp.WSGIApplication([
      ('/', MainHandler)
      ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
