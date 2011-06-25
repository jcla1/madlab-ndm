import random, string


def getString(length):

	generatedString = "".join([random.choice(string.ascii_letters + string.digits + "-") for i in xrange(length)])
    
#	thingQuery = Thing.gql('WHERE thingid = :1 LIMIT 1', generatedString)
      
	return generatedString
