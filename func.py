#!/usr/bin/env python
#
# (c) 2011 Joseph Adams

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.api import users
from models import *
import random, string, os

TEMPLATE_DIR = "templates"
THING_URL_BASE = "http://localhost:8080/"

def tpl(name):
  return os.path.join(
    os.path.dirname(__file__),
    TEMPLATE_DIR,
    name
  )


def getString(length):

  generatedString = "".join([random.choice(string.ascii_letters + string.digits + "-") for i in xrange(length)])

  return generatedString
