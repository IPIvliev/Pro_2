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
		if direction == 'forward':
			try:
				# Declare an named instance of class pass a name and motor type
				rpi_dc_lib.TB6612FNGDc.standby(Standby, True)
				
				PMotor.forward(99) # Направление (direction) может быть forward или backward
				time.sleep(0.5)
			except Exception as error:
				print(error)
				print("Unexpected error:")
			finally:
				PMotor.cleanup(False)
				rpi_dc_lib.TB6612FNGDc.standby(Standby, False)
		else:
			rpi_dc_lib.TB6612FNGDc.standby(Standby, True)
			PMotor.backward(80)
			rpi_dc_lib.TB6612FNGDc.standby(Standby, False)
		#time.sleep(5)
		#PMotor.stop(0)
