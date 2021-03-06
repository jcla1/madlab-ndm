#!/usr/bin/env python
#
# (c) 2011 Joseph Adams

from google.appengine.ext import db

class Thing(db.Model):
	title = db.StringProperty()
	author = db.StringProperty()
	thingid = db.StringProperty()
	isbn = db.StringProperty()

class Annotation(db.Model):
	thing = db.ReferenceProperty(Thing)
	comment = db.StringProperty()
#	picture
#	location
	created = db.DateTimeProperty(auto_now_add=True)
	creator = db.UserProperty()	

