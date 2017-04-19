#!/usr/bin/python

import atexit
import dweepy
import random
import signal
import sys
import time

from random import randint

datafreeboard = {}
datadweet = "activem"

def SIGINTHandler(signum, frame):
	raise SystemExit

def exitHandler():
	print("Exiting")
	time.sleep(2)
	datafreeboard['alive'] = "0"
	datafreeboard['temperature'] =  0
	datafreeboard['message'] = "None"
	datafreeboard['alert'] = "0"
	datafreeboard['longitude'] = "-74,0230171210126"
	datafreeboard['latitude'] = "4,74123914632389"
	dweepy.dweet_for(datadweet, datafreeboard)
	sys.exit(0)

atexit.register(exitHandler)
signal.signal(signal.SIGINT, SIGINTHandler)

if __name__ == '__main__':

	message = "Welcome Operator!"

	while True:

		temperature = randint(19,25)
		latitude = random.uniform(21.14000000, 21.18000000)
		longitude = random.uniform(-101.600000, -101.660000)

		datafreeboard['alive'] = "1"
		datafreeboard['temperature'] =  temperature
		datafreeboard['message'] = message
		datafreeboard['alert'] = "1"
		datafreeboard['longitude'] = latitude
		datafreeboard['latitude'] = longitude
		dweepy.dweet_for(datadweet, datafreeboard)
		time.sleep(2)
