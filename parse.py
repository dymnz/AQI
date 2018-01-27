import json
from urllib.request import urlopen


class Parser: 
	aqi_url = None
	site_name_list = []
	site_data_list = []

	def init(self, aqi_url):
		self.aqi_url = aqi_url

	def read_AQI(self): 		
		response = urlopen(self.aqi_url)
		raw_data = json.loads(response.read())
		for record in raw_data['result']['records']:
			self.site_name_list.append(record['SiteName'])
			self.site_data_list.append(record)

	def get_city(self, site_name):
		site_index = self.site_name_list.index(site_name)
		return self.site_data_list[site_index]



