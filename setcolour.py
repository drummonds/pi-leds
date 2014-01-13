"""
New Year - Celebrations display

Run as sudo python newyear.py
"""

# Light painting / POV demo for Raspberry Pi
from ledrope import leds
import time
from sys import argv

#Led functions
#!/usr/bin/python

import ledrope
import colorsys

#Logitech music system
from pylms.server import Server
from pylms.player import Player

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

def leaf_sprite(x):
	add_colour(x-1,0,60,10)
	add_colour(x  ,0,127,0)
	add_colour(x+1,0,60,10)

def berry_sprite(x):
	add_colour(x-1,127,0,0)
	add_colour(x  ,127,0,0)
	add_colour(x+1,127,0,0)

def holly_sprite(x):
	leaf_sprite(x-15)
	berry_sprite(x)
	leaf_sprite(x+15)

def forest_sprite(x):
	for i in range(60):
		add_colour(x+i-30,0,64,32)

#!/usr/bin/env python


def play_music():
	sc = Server(hostname="10.0.0.1", port=9090, username="user", password="password")
	sc.connect()
	p=sc.get_player('00:04:20:17:5b:41')
	p.playlist_play("file:///volume1/hdtl/Music/H3MusicArchive/Amazon%20MP3/Sam%20The%20Sham%20&%20The%20Pharaohs/20th%20Century%20Masters_%20The%20Millenium%20Collection_%20Best%20Of%20Sam%20The%20Sham%20&%20The%20Pharaohs/02%20-%20Lil%27%20Red%20Riding%20Hood.mp3")
	p.play()
	p.seek_to(0)

def red_riding_hood_walk():
	for i in range(ledrope.numleds):
		leds.all_one_colour()
		red_sprite(i)
		leds.write()
		time.sleep(0.1)

def red_riding_hood_forest_walk():
	for i in range(ledrope.numleds):
		leds.all_one_colour()
		red_sprite(i)
		forest_sprite(60)
		leds.write()
		time.sleep(0.1)

def red_riding_hood():
	play_music()
	red_riding_hood_walk()
	red_riding_hood_forest_walk()

def psychadelic(saturation = 0.5, value = 1):
	leds.all_one_colour()
	for i in range(ledrope.numleds):
		red, green,blue = colorsys.hsv_to_rgb(i / (ledrope.numleds-1.0),saturation,value)
		add_colour(i,int(red*127),int(green*127),int(blue*127))
	leds.write()

#Web controller
class Root(object):

	def default(self, **kwargs):
		print 'Default method:'+kwargs
		return ''

	def index(self):
        # Ask for the user's name.
		return ''

	def ledPsychadelic(self,saturation=0.5,value=1.0):
		psychadelic(float(saturation),float(value))
		return "Psychadelic lighting."

	def redLedFlash(self, name = None):
		red_riding_hood()
		leds.all_one_colour()
		leds.write()
		return "Red light goes across kitchen."

	def xmas1(self):
		leds.all_one_colour()
		for i in (20,82):
			holly_sprite(i)
		leds.write()
		return "Xmas 1"

	def setColour(self,red=0,green=0,blue=0):
		set_red = int(red)
		set_green = int(green)
		set_blue = int(blue)
		leds.all_one_colour(set_red,set_green,set_blue)
		leds.write()
		return "Set colour to %s,%s,%s." % (set_red,set_green,set_blue)

if __name__ == '__main__':
	r = Root()
	leds.blank_on_exit = False
	r.setColour(int(argv[1]),int(argv[2]),int(argv[3]))



