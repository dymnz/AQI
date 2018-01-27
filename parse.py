import json
from urllib.request import urlopen


class Parser: 
	url = None
	site_name_list = []
	site_data_list = []

	def init(self, url):
		self.url = url

	def read(self): 		
		response = urlopen(self.url)
		raw_data = json.loads(response.read())
		for record in raw_data['result']['records']:
			self.site_name_list.append(record['SiteName'])
			self.site_data_list.append(record)

	def get_city(self, site_name):
		site_index = self.site_name_list.index(site_name)
		return self.site_data_list[site_index]



