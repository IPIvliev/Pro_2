from kivy.uix.screenmanager import Screen
from Moduls.vat_stepper import VatMotor
from Moduls.led import LED

class ManageWindow(Screen):
	
	def clean_display(self):
		if self.clean_toggle.state == 'down':
			self.clean_toggle.text = 'Включено'
			LED.turn_led_on()
		elif self.clean_toggle.state == 'normal':
			self.clean_toggle.text = 'Выключено'
			LED.turn_led_off()

	def round_vat(self):
		if self.vat_round_toggle.state == 'down':
			self.vat_round_toggle.text = 'Включено'
			#VatMotor.go()
		elif self.vat_round_toggle.state == 'normal':
			self.vat_round_toggle.text = 'Выключено'
			#VatMotor.stop_moving()
