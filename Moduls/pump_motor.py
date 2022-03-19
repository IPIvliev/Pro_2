import RPi.GPIO as GPIO
import time
import Moduls.GlobalValues as GlobalValues
from RpiMotorLib import rpi_dc_lib

PWA = GlobalValues.PUMPPOWERPORT
AI1 = GlobalValues.PUMPAI1
AI2 = GlobalValues.PUMPAI1
Standby = GlobalValues.PUMPSTANDBY

Freq = 50
PMotor = rpi_dc_lib.TB6612FNGDc(AI1, AI2, PWA, Freq, False, "motor_one")
class PumpMotor():

	def pump_go(direction, delay, ti):
		#rpi_dc_lib.TB6612FNGDc.standby(Standby, True)
		stop = False
		if direction == 'forward':

			GPIO.output(Standby, True)
			#turning the gpio on and off tells the easy driver to take one step
			GPIO.output(AI1, True)
			GPIO.output(AI2, False)
			
			GPIO.output(PWA, True)
			time.sleep(0.01)
			GPIO.output(PWA, False)
	
			#Wait before taking the next step...this controls rotation speed
			time.sleep(0.01)
			#PMotor.forward(80)
			#print("Motor forward")
		else:
			PMotor.backward(80)
			print("Motor backward")
			
		#time.sleep(0.2)
		#PMotor.stop(0)
		#PMotor.cleanup(False)
		#rpi_dc_lib.TB6612FNGDc.standby(Standby, False)

	def stop_moving():
		global stop
		stop = True

	def go():
		moving = Thread(target=PumpMotor.stepper_go, args=(vat_speed, distance, direction))
		moving.daemon = True
		moving.start()