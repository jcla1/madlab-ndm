#!/usr/bin/env python
#
# (c) 2011 Joseph Adams


from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

import logging

from func import *
from models import *


class SearchHandler(webapp.RequestHandler):
    def get(self):
        query = self.request.get("query")
        
        if ( query ):
            annotations = Annotation.all()
            comments = []
            
            for a in annotations:
                if a.thing.title == query:
                    comments.append(a.comment)
            
            self.response.out.write(template.render(tpl("search.html"), {
                'comments': comments
            }))
            
        else:
            self.response.out.write(template.render(tpl("search.html"), {}))
        
def main():
    application = webapp.WSGIApplication([
      ('/search', SearchHandler)
      ],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
