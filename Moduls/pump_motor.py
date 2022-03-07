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
		rpi_dc_lib.TB6612FNGDc.standby(Standby, True)
		if direction == 'forward':
			PMotor.forward(99)
		else:
			PMotor.backward(99)
			
		time.sleep(0.2)
		PMotor.stop(0)
		PMotor.cleanup(False)
		rpi_dc_lib.TB6612FNGDc.standby(Standby, False)
