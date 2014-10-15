import pusherclient
import time
import json
import math
import led_controller
from led_controller import LightEnum
global pusher

def connect_handler(data):
    channel = pusher.subscribe('windTurbine')
    channel.bind('power', process)

def process(power):
	decoded = json.loads(power)
	print ('power')
	print (decoded['power'] )
	green = math.floor((float(decoded['power']) / 2500 * 100))

	red = 100-green

        #fudge led brightness
        #green = green*0.3
	
	#red = 100-green
	
	print ("turbine (green):")
	print (green)
	print ("red:")
	print (red)
	controller.displayLEDColour(LightEnum.red, red)
	controller.displayLEDColour(LightEnum.green, green)



time.sleep(20)
pusher = pusherclient.Pusher('<apikey>')
pusher.connection.bind('pusher:connection_established', connect_handler)
pusher.connect()

controller = led_controller.LEDController(7 ,12 )

controller.displayLEDColour(LightEnum.red, 100)
controller.displayLEDColour(LightEnum.green, 50)


while True:
    time.sleep(1)

