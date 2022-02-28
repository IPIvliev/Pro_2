import time
#import RPi.GPIO as GPIO
from RpiMotorLib import rpi_dc_lib

# ====== tests for  DC motor driven by TB6612FNG ====
# TB66 -- GPIO RPI
PWA = 26
AI1 = 13
AI2 = 19
#PWB = 18
#BI1 = 23
#BI2 = 24
Standby = 6

Freq = 50

# Declare an named instance of class pass a name and motor type
PMotor = rpi_dc_lib.TB6612FNGDc(AI1, AI2, PWA, Freq, False, "pump_motor")

class PumpMotor():

	def pump_go(direction, delay, ti):
		if direction == 'forward':
			PMotor.forward(80) # Направление (direction) может быть forward или backward
		else:
			PMotor.backward(80)
		time.sleep(delay)
		PMotor.stop(0)
