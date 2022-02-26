import RPi.GPIO as GPIO
from Moduls.door_stepper import DoorMotor

class OpenDoor():

	def open_door(self, signal=2):

		if signal == 1:
			self.screens[0].ids.door_toggle.text = 'Открыто'
			self.screens[0].ids.door_toggle.state = 'down'
			DoorMotor.go()
		elif signal == 0:
			self.screens[0].ids.door_toggle.text = 'Закрыто'
			self.screens[0].ids.door_toggle.state = 'normal'
			DoorMotor.go()
		else:
			if self.screens[0].ids.door_toggle.state == 'down':
				self.screens[0].ids.door_toggle.text = 'Открыто'
				DoorMotor.go()
			else:
				self.screens[0].ids.door_toggle.text = 'Закрыто'
				DoorMotor.go()
