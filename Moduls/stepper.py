import time
import Moduls.GlobalValues as GlobalValues
from RpiMotorLib import RpiMotorLib

GPIO_pins = (-1, -1) # Microstep Resolution MS1-MS2 -> GPIO Pin

motor_direction = GlobalValues.ZMD
step = GlobalValues.ZMS

class Motor():

# call the function pass the parameters
	def stepper_go(speed, distance, direction):
		mymotortest = RpiMotorLib.A3967EasyNema(motor_direction, step, GPIO_pins)
		time.sleep(0.1)
		mymotortest.motor_move(speed, distance, direction, False, "Full", .05)