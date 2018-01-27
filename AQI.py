from util import *
from parse import Parser

setup_logger()
logging.info('AQI initializing...')


parser = Parser()
parser.init('https://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-000259?sort=SiteName&offset=0&limit=1000')
parser.read()
parser.get_city('新竹')