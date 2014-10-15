import sys
import time

import RPi.GPIO as GPIO

class LightEnum:
	red = 1
	green = 2
	blue = 3

class LEDController:
	pr = None
	pg = None
	pb = None

	prDuty = 0
	pgDuty = 0
	pbDuty = 0

	def __init__(self, redPin = -1, greenPin = -1, bluePin = -1):
		#enable GPIO stuff
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BOARD)
	
		#red LED
		if redPin != -1 :
			GPIO.setup(redPin, GPIO.OUT)
			self.pr = GPIO.PWM(redPin, 70)
			self.pr.start(0) 
		#green LED
		if greenPin != -1 :
			GPIO.setup(greenPin, GPIO.OUT)
			self.pg = GPIO.PWM(greenPin, 70)
			self.pg.start(0)
		#blue LED
		if bluePin != -1 :
			GPIO.setup(bluePin, GPIO.OUT)
			self.pb = GPIO.PWM(bluePin, 50)
			self.pb.start(0)
	
	def dispose(self):
		if self.pg != None :
			self.pg.stop()
		if self.pr != None :
			self.pr.stop()
		if self.pb != None :
			self.pb.stop()

		#finally, clean GPIO
		GPIO.cleanup()

		
	def displayLEDColour( self, colour, percent ):
		if percent > 100:
			percent = 100
		elif percent < 0:
			percent = 0

		#change duty cycle of specified channel	
		if colour == LightEnum.red and self.prDuty != percent:
			self.pr.ChangeDutyCycle(percent)
			self.prDuty = percent
			print("[db] Red duty is at %d" % percent)
		elif colour == LightEnum.blue and self.pbDuty != percent:
			self.pb.ChangeDutyCycle(percent)
			self.pbDuty = percent
			print("[db] Blue duty is at %d" % percent)
		elif colour == LightEnum.green and self.pgDuty != percent:
			self.pg.ChangeDutyCycle(percent)
			self.pgDuty = percent
			print("[db] Green duty is at %d" % percent)
	
	def getDCValue( self, value, max ):
		return (value / max) * 100
	


