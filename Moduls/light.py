import Moduls.GlobalValues as GlobalValues

test = GlobalValues.TEST
light_port = GlobalValues.LIGHT_PORT

if test == 0:
  import RPi.GPIO as GPIO

class Light():

	def light(self, signal=2):
		if test == 0:
			#GPIO.setmode(GPIO.BCM)
			GPIO.setup(light_port, GPIO.OUT)	

		global LIGHT
		if signal == 1:
			self.screens[0].ids.light_toggle.text = 'Включено'
			self.screens[0].ids.light_toggle.state = 'down'
			if test == 0:
				GPIO.output(light_port, True)
			else:
				pass
			#GPIO.cleanup()
		elif signal == 0:
			self.screens[0].ids.light_toggle.text = 'Выключено'
			self.screens[0].ids.light_toggle.state = 'normal'
			if test == 0:
				GPIO.output(light_port, False)
			else:
				pass	
		else:
			if self.screens[0].ids.light_toggle.state == 'down':
				self.screens[0].ids.light_toggle.text = 'Включено'
				if test == 0:
					GPIO.output(light_port, True)
				else:
					pass
			else:
				self.screens[0].ids.light_toggle.text = 'Выключено'
				if test == 0:
					GPIO.output(light_port, False)
				else:
					pass