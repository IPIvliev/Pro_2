from kivy.uix.screenmanager import Screen
from Moduls.light import Light


class MainWindow(Screen):

	def turn_light(self):
		Light.light(self.parent)
