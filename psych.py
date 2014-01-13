#!/usr/bin/python

# Light painting / POV demo for Raspberry Pi

from ledrope import leds
import time

# sample code
while True:
	leds.all_one_colour(127,100,0)
	leds.write()
	time.sleep(0.1)
	leds.all_one_colour(127,0,0)
	leds.write()
	time.sleep(2)
	leds.all_one_colour(0,0,0)
	leds.write()
	time.sleep(1)

