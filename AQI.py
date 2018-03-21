import json
import datetime, schedule, time

from util import *
from analysis import *

from parse import Parser
from notification import Notification


setup_logger(console_log_level = logging.INFO, file_log_level = logging.DEBUG)
logging.info('[Info] Initializing...')


logging.info('[Info] Loading settings from setting.json')
try:
	with open('setting.json') as setting_json:
		setting = json.load(setting_json)
		logging.debug('[Debug] setting: {}'.format(setting))
except:
	logging.error('[Error] Can\'t read setting')
	logging.critical('Now TERMINATING!')
	exit()

logging.info('[Info] Loading credentials from credential.json')
try:
	with open('credential.json') as credential_json:
		credential = json.load(credential_json)
		logging.debug('[Debug] Credential read')
except:
	logging.error('[Error] Can\'t read credential')
	logging.critical('Now TERMINATING!')
	exit()

parser = Parser()
parser.init('http://opendata2.epa.gov.tw/AQI.json')

notification = Notification()
notification.init(credential)

# send_pushed_notification(credential['pushed'], '☁ asdasds')

def check_and_notify(site_name):
	try: 
		parser.get_dataset()
		data = parser.get_city(site_name)

		logging.debug('[Debug] Got data for {}'.format(site_name))

		scaled_AQI = AQI_scaling(int(data['AQI']))

		logging.debug('[Debug] Scaled AQI for {}: {}'.format(site_name, scaled_AQI))

		notification.send_pushed(site_name + ':' + '🔥' * scaled_AQI)


	except ValueError as error:
		logging.error('[Error] Can\'t retrieve AQI data for {}\n Error: {}'.format(site_name, error.args))
		notification.send_pushed('[Error] Can\'t retrieve AQI data for {}'.format(site_name))


scheduled_job_list = []
for request in setting['requests']:
	for scheduled_time in request['time']:
		scheduled_job_list.append((scheduled_time, request['site_name']))

for scheduled_job in scheduled_job_list:
	schedule.every().day.at(scheduled_job[0]).do(check_and_notify, scheduled_job[1])

logging.info('[Info] Wait until scheduled time')

while True:
	schedule.run_pending()
	time.sleep(1)

