from kivy.uix.screenmanager import Screen
from Moduls.pump_motor import PumpMotor
from kivy.clock import Clock
from functools import partial
from threading import Thread
from Moduls.scale import Scale

class VatManageWindow(Screen):
	def on_enter(self):
		self.ids.scale_value.text = "0.00"
		Clock.schedule_interval(partial(VatManageWindow.start_scale), 0.1)
		

	def pour_in(self):
		self.event = Clock.schedule_interval(partial(PumpMotor.pump_go, 'forward'), 0.002)

	def pour_out(self):
		self.event = Clock.schedule_interval(partial(PumpMotor.pump_go, 'backward'), 0.002)

	def pour_stop(self):
		self.event.cancel()
		self.event = Clock.schedule_once(partial(PumpMotor.pump_stop), 0.01)

	def start_scale(ti):
		sample = Scale.readCount()
		w = sample/106
		self.ids.scale_value.text = str(w)
		time.sleep(0.1)