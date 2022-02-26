from kivy.uix.screenmanager import Screen
from Moduls.open_door import OpenDoor
from Moduls.light import Light


class MainWindow(Screen):

	def open_door(self):
		OpenDoor.open_door(self.parent)

	def turn_light(self):
		Light.light(self.parent)
