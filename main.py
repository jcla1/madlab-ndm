#!/usr/bin/env python
#
# (c) 2011 Joseph Adams


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util, template
from google.appengine.api import users

from func import *

class MainHandler(webapp.RequestHandler):
    def get(self):
	    self.response.out.write(
          template.render(tpl('testpage.html'), {
	            'loginurl':	users.create_login_url('/'),
	            'logouturl': users.create_logout_url('/')
               })
      )
      

def main():
    application = webapp.WSGIApplication([
      ('/', MainHandler)
      ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
