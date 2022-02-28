import time
#import RPi.GPIO as GPIO
from RpiMotorLib import rpi_dc_lib

# ====== tests for  DC motor driven by TB6612FNG ====
# TB66 -- GPIO RPI
PWA = 26
AI1 = 13
AI2 = 19
Standby = 6

Freq = 50
PMotor = rpi_dc_lib.TB6612FNGDc(AI1, AI2, PWA, Freq, False, "motor_one")
class PumpMotor():

	def pump_go(direction, delay, ti):
		rpi_dc_lib.TB6612FNGDc.standby(Standby, True)
		if direction == 'forward':
			PMotor.forward(99)
		else:
			PMotor.backward(99)
			
		time.sleep(0.1)
		PMotor.stop(0)
		PMotor.cleanup(False)
		rpi_dc_lib.TB6612FNGDc.standby(Standby, False)
