from kivy.uix.screenmanager import Screen
from Moduls.pump_motor import PumpMotor
from kivy.clock import Clock
from functools import partial

class VatManageWindow(Screen):
	def pour_in(self):
		print("Clock motor GO")
		#Clock.schedule_once(partial(PumpMotor.pump_go, 'forward', 0.1), 0.1)
		#self.event = Clock.schedule_interval(partial(PumpMotor.pump_go, 'forward', 0.1), 0.1)
		PumpMotor.pump_go('forward', 0.5, 0.1)

	def pour_out(self):
		self.event = Clock.schedule_interval(partial(PumpMotor.pump_go, 'backward', 0.1), 0.1)
		#PumpMotor.pump_go('backward', 0.1)

	def stop_pressing(self):
		#PMotor.stop(0)
		pass