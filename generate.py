#!/usr/bin/env python
#
# (c) 2011 Joseph Adams


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

import logging

from func import *


class GenerateThingHandler(webapp.RequestHandler):
    def get(self):
        thingquery = getString(20)
        query = Thing.gql('WHERE thingid = :1 LIMIT 1', thingquery)
	if query.count() == 1:
            qrcode_link = '<img src="http://chart.apis.google.com/chart?cht=qr&chs=250x250&chld=M&chl='+ THING_URL_BASE + 'thing/' + thingquery + '" />'
            thing_link = THING_URL_BASE + 'thing/' + thingquery
          
            self.response.out.write(
                template.render(tpl('generate.html'), {
                    'qrimg': qrcode_link,
                    'thing_link': thing_link,
    	            'loginurl':	users.create_login_url('/'),
    	            'logouturl': users.create_logout_url('/')
                     })
            )
          
        else:
          thing = Thing()
          thing.thingid = thingquery
          thing.put()
          
          qrcode_link = '<img src="http://chart.apis.google.com/chart?cht=qr&chs=250x250&chld=M&chl='+ THING_URL_BASE + 'thing/' + thingquery + '" />'
          thing_link = THING_URL_BASE + 'thing/' + thingquery

          
          self.response.out.write(
              template.render(tpl('generate.html'), {
                  'qrimg': qrcode_link,
                  'thing_link': thing_link,
    	            'loginurl':	users.create_login_url('/'),
    	            'logouturl': users.create_logout_url('/')
                   })
          )

def main():
    application = webapp.WSGIApplication([
      ('/generate', GenerateThingHandler)
      ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
