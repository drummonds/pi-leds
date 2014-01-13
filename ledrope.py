#!/usr/bin/python

# Light painting / POV demo for Raspberry Pi using
# Adafruit Digital Addressable RGB LED flex strip.
# ----> http://adafruit.com/products/306

import RPi.GPIO as GPIO
import time

# Configurable values
dev       = "/dev/spidev0.0"

# Open SPI device, load image in RGB format and get dimensions:
spidev    = file(dev, "wb")
numleds	= 103
print "%dx pixels" % numleds

# Calculate gamma correction table.  This includes
# LPD8806-specific conversion (7-bit color w/high bit set).
gamma = bytearray(256)
for i in range(256):
	gamma[i] = 0x80 | int(pow(float(i) / 255.0, 2.5) * 127.0 + 0.5)

# Then it's a trivial matter of writing each column to the SPI port.
# going to iterate through all the colours

class LedRope(object):
	next_led = bytearray(numleds * 3 + 1)
	blank_on_exit = True

	#Pattern definition 
	def all_one_colour(self,set_red=0,set_green=0,set_blue=0):
		r = 128 | set_red
		g = 128 | set_green
		b = 128 | set_blue

		for i in range(numleds):
			i3 = i * 3
			self.next_led[i3 + 0] = g
			self.next_led[i3 + 1] = r
			self.next_led[i3 + 2] = b

	def write(self,array = next_led):
		spidev.write(self.next_led)
		spidev.flush()

	def __del__(self):
		print (" Blank on exit = {}".format(self.blank_on_exit))
		if self.blank_on_exit :
			print("Blanking display")
			self.all_one_colour(0,0,0)
       			self.write()


leds = LedRope()

leds.all_one_colour(0,0,0)
leds.write()

print "Led setup finished"

# sample code
if __name__ == "__main__":
	while True:
		leds.all_one_colour(127,0,0)
		leds.write()
		time.sleep(0.001)

