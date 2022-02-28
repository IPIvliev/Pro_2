from kivy.uix.screenmanager import Screen
from Moduls.pump_motor import PumpMotor
from kivy.clock import Clock
from functools import partial

class VatManageWindow(Screen):
	def pour_in(self):
		print("Clock motor GO")
		self.event = Clock.schedule_interval(partial(PumpMotor.pump_go, 'forward', 1), 1)
		#PumpMotor.pump_go('forward', 0.1)

	def pour_out(self):
		self.event = Clock.schedule_interval(partial(PumpMotor.pump_go, 'backward', 1), 1)
		#PumpMotor.pump_go('backward', 0.1)

	def stop_pressing(self):
		self.event.cancel()