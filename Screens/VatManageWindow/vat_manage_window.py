from kivy.uix.screenmanager import Screen
from Moduls.pump_motor import PumpMotor
from kivy.clock import Clock
from functools import partial
from threading import Thread
from Moduls.scale import Scale

class VatManageWindow(Screen):
	def on_enter(self):
		self.ids.scale_value.text = "0.00"
		scale_value = Clock.schedule_interval(partial(Scale.readCount), 1)
		self.ids.scale_value.text = str(scale_value)

	def pour_in(self):
		self.event = Clock.schedule_interval(partial(PumpMotor.pump_go, 'forward'), 0.002)

	def pour_out(self):
		self.event = Clock.schedule_interval(partial(PumpMotor.pump_go, 'backward'), 0.002)

	def pour_stop(self):
		self.event.cancel()
		self.event = Clock.schedule_once(partial(PumpMotor.pump_stop), 0.01)