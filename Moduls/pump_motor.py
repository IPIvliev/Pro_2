import RPi.GPIO as GPIO
import time
import Moduls.GlobalValues as GlobalValues

PWA = GlobalValues.PUMPPOWERPORT
AI1 = GlobalValues.PUMPAI1
AI2 = GlobalValues.PUMPAI2
Standby = GlobalValues.PUMPSTANDBY

class PumpMotor():

	def pump_go(direction, delay, ti):
		stop = False
		GPIO.output(Standby, True)
		if direction == 'forward':

			GPIO.output(AI1, True)
			GPIO.output(AI2, False)
			
			GPIO.output(PWA, True)
			time.sleep(0.0002)

		else:
			GPIO.output(AI1, False)
			GPIO.output(AI2, True)
			
			GPIO.output(PWA, True)
			time.sleep(0.0002)		