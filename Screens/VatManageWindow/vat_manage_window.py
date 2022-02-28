from kivy.uix.screenmanager import Screen
from Moduls.pump_motor import PumpMotor
from kivy.clock import Clock
from functools import partial
from threading import Thread

class VatManageWindow(Screen):
	def pour_in(self):
		print("Clock motor GO")
		#self.event = Clock.schedule_interval(partial(PumpMotor.pump_go, 'forward', 0.1), 0.1)
		#Clock.schedule_once(partial(PumpMotor.pump_go, 'forward', 0.1), 0.3)
		moving = Thread(target=PumpMotor.pump_go, args=('forward', 0.1))
		moving.daemon = False
		moving.start()

	def pour_out(self):
		self.event = Clock.schedule_interval(partial(PumpMotor.pump_go, 'backward', 0.1), 0.1)

	def pour_stop(self):
		self.event.cancel()