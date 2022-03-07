import Moduls.GlobalValues as GlobalValues

test = GlobalValues.TEST
light_port = GlobalValues.LIGHT_PORT

class Light():

	def light(self, signal=2):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(light_port, GPIO.OUT)	

		global LIGHT
		if signal == 1:
			self.screens[0].ids.light_toggle.text = 'Включено'
			self.screens[0].ids.light_toggle.state = 'down'
			GPIO.output(light_port, True)
			#GPIO.cleanup()
		elif signal == 0:
			self.screens[0].ids.light_toggle.text = 'Выключено'
			self.screens[0].ids.light_toggle.state = 'normal'
			GPIO.output(light_port, False)
		else:
			if self.screens[0].ids.light_toggle.state == 'down':
				self.screens[0].ids.light_toggle.text = 'Включено'
				GPIO.output(light_port, True)
			else:
				self.screens[0].ids.light_toggle.text = 'Выключено'
				GPIO.output(light_port, False)
