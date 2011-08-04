#!/usr/bin/env python
#
# (c) 2011 Joseph Adams


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util, template
from google.appengine.api import users

from func import *
from models import *
from django.utils import simplejson as json
import urllib2, logging

class ISBNHandler(webapp.RequestHandler):
    def get(self):
        isbn = self.request.get("isbn")
        thingid = self.request.get("thingid")
        
        isbn = urllib2.quote(isbn)
        res = urllib2.urlopen("https://www.googleapis.com/books/v1/volumes?q=" + isbn)
        json_data = res.read()
        
        data = json.loads(json_data)
        
        if data['items']:
            title = data['items'][0]['volumeInfo']['title']
            author = data['items'][0]['volumeInfo']['authors']
        

            if type(author) == list:
                authors = ''
                authors = ", ".join(author)
                author = authors
        
            logging.info("ISBN: %s" % isbn)
            logging.info("ThingID: %s" % thingid)
            logging.info("Title: %s" % title)
            logging.info("Author: %s" % author)

        
            t = Thing.all().filter("thingid =", thingid).get()
            if t.title == None:
                t.title = title
                t.author = authors
                t.isbn = isbn
                t.put()
            else:
                self.error(500)
        



def main():
    application = webapp.WSGIApplication([
      ('/isbn', ISBNHandler)
      ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
