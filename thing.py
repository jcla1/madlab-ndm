#!/usr/bin/env python
#
# (c) 2011 Joseph Adams


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

import logging

from func import *

THING_URL_BASE = "http://192.168.0.90:8080/"


class GenerateThingHandler(webapp.RequestHandler):
    def get(self):
        thingquery = getString(20)
        query = Thing.gql('WHERE thingid = :1 LIMIT 1', thingquery)
	if query.count() == 1:
          self.response.out.write('<img src="http://chart.apis.google.com/chart?cht=qr&chs=250x250&chld=M&chl='+ THING_URL_BASE + 'thing/' + thingquery + '" />')
          self.response.out.write(thingquery)
        else:
          thing = Thing()
          thing.thingid = thingquery
          thing.put()
          self.response.out.write('<img src="http://chart.apis.google.com/chart?cht=qr&chs=250x250&chld=M&chl='+ THING_URL_BASE + 'thing/' + thingquery + '" />')
          self.response.out.write("<br /><a href='%sthing/%s'>%s</a>" % (THING_URL_BASE, thingquery, thingquery))



class ThingHandler(webapp.RequestHandler):
    def get(self, passedid):
      query = Thing.gql('WHERE thingid = :1 LIMIT 1', passedid)
      
      if (query.count() == 0):
        self.response.out.write("The id you passed does not exist.")
      else:
        
        if (query.fetch(1)[0].title == None):
          # Now display a form for adding info.
          self.response.out.write(
              template.render(tpl('infoandform.html'), {
  		            'loginurl':	users.create_login_url('/'),
  		            'logouturl': users.create_logout_url('/')
  	               })
  	          )
        else:
          result = query.fetch(1)
          annotations = Annotation().all().filter('thing =', result[0]).order("-created").fetch(999)
          logging.info("thing: %s" % result[0])
          logging.info("annotations: %s" % annotations)
          # Just display the info to the user.
          self.response.out.write(
              template.render(tpl('infoandform.html'), {
                  'info': {'annotations': annotations,'title': result[0].title, 'author': result[0].author, 'thingid': passedid},
  		            'loginurl':	users.create_login_url('/'),
  		            'logouturl': users.create_logout_url('/')
  	               })
  	          )

    def post(self, passedid):
      title = self.request.get('title')
      author = self.request.get('author')

      newthing = Thing().all().filter("thingid =", passedid).fetch(1)
      newthing[0].title = title
      newthing[0].author = author
      newthing[0].put()


def main():
    application = webapp.WSGIApplication([
      ('/thing/generate', GenerateThingHandler),
      ('/thing/(.*)', ThingHandler)
      ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
