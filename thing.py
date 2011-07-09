#!/usr/bin/env python
#
# (c) 2011 Joseph Adams


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

from func import *

THING_URL_BASE = "http://localhost:8080/"


class GenerateThingHandler(webapp.RequestHandler):
    def get(self):
        thingquery = getString(20)
	if thingquery[0].count() == 1:
          self.response.out.write('<img src="http://chart.apis.google.com/chart?cht=qr&chs=250x250&chld=M&chl='+ THING_URL_BASE + thingquery[0][0].thingid + '" />')
        else:
          thing = Thing()
          thing.thingid = thingquery[1]
          thing.put()
          self.response.out.write('<img src="http://chart.apis.google.com/chart?cht=qr&chs=250x250&chld=M&chl='+ THING_URL_BASE + thingquery[0][0].thingid + '" />')

class ThingHandler(webapp.RequestHandler):
    def get(self, passedid):
      query = Thing.gql('WHERE thingid = :1 LIMIT 1', passedid)
      
      if (query.count() == 0):
        self.response.out.write("The id you passed does not exist.")
      else:
        query = Thing.gql('WHERE thingid = :1 AND title = :2 LIMIT 1', passedid, None)
        
        if (query.count() == 0):
          # Now display a form for adding info.
          self.response.out.write(
              template.render(tpl('infoandform.html'), {
  		            'loginurl':	users.create_login_url('/'),
  		            'logouturl': users.create_logout_url('/')
  	               })
  	          )
        else:
          # Just display the info to the user.
          self.response.out.write(
              template.render(tpl('infoandform.html'), {
                  'info': {title:q}
  		            'loginurl':	users.create_login_url('/'),
  		            'logouturl': users.create_logout_url('/')
  	               })
  	          )
      

def main():
    application = webapp.WSGIApplication([
      ('/thing/generate', GenerateThingHandler),
      ('/thing/(.*)', ThingHandler)
      ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
