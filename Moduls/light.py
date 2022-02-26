import RPi.GPIO as GPIO

light = 18

class Light():

	def light(self, signal=2):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(light, GPIO.OUT)	

		global LIGHT
		if signal == 1:
			self.screens[0].ids.light_toggle.text = 'Включено'
			self.screens[0].ids.light_toggle.state = 'down'
			GPIO.output(light, True)
			#GPIO.cleanup()
		elif signal == 0:
			self.screens[0].ids.light_toggle.text = 'Выключено'
			self.screens[0].ids.light_toggle.state = 'normal'
			GPIO.output(light, False)
		else:
			if self.screens[0].ids.light_toggle.state == 'down':
				self.screens[0].ids.light_toggle.text = 'Включено'
				GPIO.output(light, True)
			else:
				self.screens[0].ids.light_toggle.text = 'Выключено'
				GPIO.output(light, False)
