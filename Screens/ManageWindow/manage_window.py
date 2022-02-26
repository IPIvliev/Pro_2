from kivy.uix.screenmanager import Screen
from Moduls.vat_stepper import VatMotor

class ManageWindow(Screen):
	
	def clean_display(self):
		if self.clean_toggle.state == 'down':
			self.clean_toggle.text = 'Включено'
		elif self.clean_toggle.state == 'normal':
			self.clean_toggle.text = 'Выключено'

	def round_vat(self):
		if self.vat_round_toggle.state == 'down':
			self.vat_round_toggle.text = 'Включено'
			VatMotor.go()
		elif self.vat_round_toggle.state == 'normal':
			self.vat_round_toggle.text = 'Выключено'
			VatMotor.stop_moving()
