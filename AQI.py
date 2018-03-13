import json
import datetime, schedule, time

from util import *
from parse import Parser


setup_logger(console_log_level = logging.INFO, file_log_level = logging.DEBUG)
logging.info('AQI initializing')

logging.info('Loading settings from setting.json')
with open('setting.json') as setting_json:
	setting = json.load(setting_json)
	logging.debug('setting: {}'.format(setting))

logging.info('Loading credentials from credential.json')
with open('credential.json') as credential_json:
	credential = json.load(credential_json)
	logging.debug('EPA token: {}'.format(credential['api_keys']['epa']))
	logging.debug('Twilio token: {}'.format(credential['api_keys']['twilio']))


parser = Parser()
parser.init('http://opendata2.epa.gov.tw/AQI.json')
parser.read_AQI()


try: 
	data = parser.get_city('新竹')
	print(data)
except:
	print('except')

def job():
	global setting
	current_time = datetime.datetime.now().strftime("%H:%M:%S")
	for request in setting['requests']:
		for scheduled_time in request['time']:
			if current_time == str(scheduled_time):
				logging.info('scheduled job for {} @ {}'.format(request['site_name'], scheduled_time))


def sc(site_name):
	try: 
		data = parser.get_city(site_name)
		print(data)
	except:
		print('except')

scheduled_job_list = []
for request in setting['requests']:
	for scheduled_time in request['time']:
		scheduled_job_list.append((scheduled_time, request['site_name']))


for scheduled_job in scheduled_job_list:
	schedule.every().day.at(scheduled_job[0]).do(sc, scheduled_job[1])

while True:
	schedule.run_pending()
	time.sleep(1)

