import requests

from util import *

class Notification:
	pushed_credential = []
	twilio_credential = []

	def init(self, credential):
		self.pushed_credential = credential['pushed']
		self.twilio_credential = credential['twilio']

	def send_pushed(self, message):
		payload = {
		  "app_key": self.pushed_credential['app_key'],
		  "app_secret": self.pushed_credential['app_secret'],
		  "target_type": self.pushed_credential['target_type'],
		  "content": message
		}

		response = requests.post("https://api.pushed.co/1/push", data=payload)

		if response.status_code != 200: 
			logging.error('[Error] Pushed notification error: {}'.format(response))
		else:
			logging.debug('[Debug] Pushed notification sent')

	def send_twilio(self, message):
		# TODO
		pass
