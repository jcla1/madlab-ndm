#!/usr/bin/env python
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

from func import *


class MainHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(getString(20))


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
