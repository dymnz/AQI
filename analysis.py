from util import *



def AQI_scaling(aqi):
	if 0 <= aqi <= 50:
		return 1
	if 51 <= aqi <= 100:
		return 2
	if 101 <= aqi <= 150:
		return 3
	if 151 <= aqi <= 200:
		return 4
	if 201 <= aqi <= 300:
		return 5
	if 301 <= aqi <= 500:
		return 6;

	raise ValueError('AQI cannot be interpreted')