#!/usr/bin/python

import ledrope
from ledrope import leds
import time

def add_colour(x,set_red,set_green,set_blue):
	if x>=0 and x<ledrope.numleds:
		i3=x*3
		leds.next_led[i3+0] = 128 | max(set_green,leds.next_led[i3+0] & 127)
		leds.next_led[i3+1] = 128 | max(set_red  ,leds.next_led[i3+1] & 127)
		leds.next_led[i3+2] = 128 | max(set_blue ,leds.next_led[i3+2] & 127)

def red_sprite(x):
	add_colour(x-2,32,0,0)
	add_colour(x-1,64,0,0)
	add_colour(x  ,127,0,0)
	add_colour(x+1,64,0,0)
	add_colour(x+2,32,0,0)

def red_riding_hood():
	for i in range(ledrope.numleds):
		leds.all_one_colour()
		red_sprite(i)
		leds.write()
		time.sleep(0.1)

# sample code
while True:
	red_riding_hood()
	leds.all_one_colour()
	leds.write()
	time.sleep(10)

