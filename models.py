from google.appengine.ext import db

class Thing(db.Model):
	title = db.StringProperty()
	author = db.StringProperty()
	thingid = db.StringProperty()
#	isbn

class Annotation(db.Model):
	thing = db.ReferenceProperty(Thing)
	comment = db.StringProperty()
#	picture
#	location
	created = db.DateTimeProperty(auto_now_add=True)
	creator = db.ReferenceProperty(User)	

class User(db.Model):
	name = db.StringProperty()
	email = db.EmailProperty()
	nickname = db.StringProperty()
