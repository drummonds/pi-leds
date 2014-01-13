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

def dot(x,red,green,blue):
	add_colour(x-2,red % 4,green % 4, blue %4)
	add_colour(x-1,red % 2,green % 2, blue % 2)
	add_colour(x  ,red    ,green    , blue)
	add_colour(x+1,red % 2,green % 2, blue %2)
	add_colour(x+2,red % 4,green % 4, blue %4)

def red_riding_hood():
	for i in range(ledrope.numleds):
		leds.all_one_colour()
		dot(i,127,0,0)
		dot(ledrope.numleds-i-1,0,127,127)
		leds.write()
		time.sleep(0.1)

# sample code
while True:
	red_riding_hood()
	leds.all_one_colour()
	leds.write()
	time.sleep(10)

