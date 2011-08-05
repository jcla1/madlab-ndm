#!/usr/bin/env python
#
# (c) 2011 Joseph Adams


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

import logging

from func import *
from models import *


class GenerateThingHandler(webapp.RequestHandler):
    def get(self):
        thingquery = getString(20)
        query = Thing.gql('WHERE thingid = :1 LIMIT 1', thingquery)
	if query.count() == 1:
            qrcode_link = '<img src="http://chart.apis.google.com/chart?cht=qr&chs=150x150&chld=M&chl='+ THING_URL_BASE + 'thing/' + thingquery + '" />'
            thing_link = THING_URL_BASE + 'thing/' + thingquery
          
            self.response.out.write(qrcode_link)
          
        else:
          thing = Thing()
          thing.thingid = thingquery
          thing.put()
          
          qrcode_link = '<img src="http://chart.apis.google.com/chart?cht=qr&chs=150x150&chld=M&chl='+ THING_URL_BASE + 'thing/' + thingquery + '" />'
          thing_link = THING_URL_BASE + 'thing/' + thingquery

          
          self.response.out.write(qrcode_link)
          
    def post(self):
        q = Thing.all().fetch(9999)
        for i in q:
            i.delete()
        self.response.out.write("ok")

def main():
    application = webapp.WSGIApplication([
      ('/lots', GenerateThingHandler)
      ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
