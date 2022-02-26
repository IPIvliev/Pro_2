import time
#import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GPIO_pins = (-1, -1) # Microstep Resolution MS1-MS2 -> GPIO Pin
motor_direction = 16       # Direction -> GPIO Pin
step = 20    # Step -> GPIO Pin

# Declare an named instance of class pass a name and motor type


class Motor():

# call the function pass the parameters
	def stepper_go(speed, distance, direction):
		mymotortest = RpiMotorLib.A3967EasyNema(motor_direction, step, GPIO_pins)
		time.sleep(0.1)
		mymotortest.motor_move(speed, distance, direction, False, "Full", .05)

# good practise to cleanup GPIO at some point before exit
		#GPIO.cleanup()
