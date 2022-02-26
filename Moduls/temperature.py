from random import randint
#import time, threading
from kivy.clock import Clock
from functools import partial


class Temperature():

	def getTemperature(self, ti):
		t = randint(18, 25)
		temp_out = str(t) + 'C°'

		self.screens[0].ids.temp_label.text = str(temp_out)
		self.screens[1].ids.temp_label.text = str(temp_out)
		self.screens[2].ids.temp_label.text = str(temp_out)
		self.screens[3].ids.temp_label.text = str(temp_out)
		self.screens[4].ids.temp_label.text = str(temp_out)
		self.screens[5].ids.temp_label.text = str(temp_out)
		self.screens[6].ids.temp_label.text = str(temp_out)
		self.screens[7].ids.temp_label.text = str(temp_out)
		self.screens[8].ids.temp_label.text = str(temp_out)
		self.screens[9].ids.temp_label.text = str(temp_out)
		self.screens[10].ids.temp_label.text = str(temp_out)

	def t(self):
		Clock.schedule_interval(partial(Temperature.getTemperature, self), 5)
