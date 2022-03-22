from kivy.uix.screenmanager import Screen
from Moduls.light import Light
import threading

class MainWindow(Screen):

	def turn_light(self):
		Light.light(self.parent)
		n_thread =  threading.active_count()
		print(n_thread)