from language_codes import LC_ENGLISH
import urllib2, urllib, json
from response_codes import RESPONSE_OK

class SimSimiException(Exception):
	pass

class SimSimi(object):

	def __init__(self, *args, **kwargs):
		self.conversation_request_url = kwargs.get('conversation_request_url','http://api.simsimi.com/request.p')
		self.conversation_key = kwargs.get('conversation_key','')
		self.conversation_language = kwargs.get('conversation_language', LC_ENGLISH)
		self.conversation_filter = kwargs.get('conversation_filter','0.0')

	def getConversation(self, text):

		requestParam = {
			'key':self.conversation_key,
			'lc':self.conversation_language,
			'ft':self.conversation_filter,
			'text':text
		}

		requestUrl = "%s?%s" % (self.conversation_request_url, urllib.urlencode(requestParam))

		response = urllib2.urlopen(requestUrl)
		responseDict = json.loads(str(response.read()))

		if responseDict['result'] != RESPONSE_OK:
			raise SimSimiException("SimSimiException occured: %s" % responseDict['msg'])

		return responseDict