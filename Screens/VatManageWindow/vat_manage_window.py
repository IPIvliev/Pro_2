from kivy.uix.screenmanager import Screen
from Moduls.pump_motor import PumpMotor
from kivy.clock import Clock
from functools import partial
from Moduls.scale import Scale
import time
import asyncio

class VatManageWindow(Screen):
	def on_enter(self):
		scale = Scale.readCount()
		self.ids.scale_value.text = "0.00"
		global EVENT
		#EVENT = Clock.schedule_interval(partial(VatManageWindow.start_scale, self, scale), 1)
		ioloop = asyncio.get_event_loop()
		tasks = [
			ioloop.create_task(VatManageWindow.start_scale(self, scale))
		]
		ioloop.run_until_complete(asyncio.wait(tasks))
		ioloop.close()
	
	def on_pre_leave(self):
		global EVENT
		#EVENT.cancel()

	def pour_in(self):
		self.event = Clock.schedule_interval(partial(PumpMotor.pump_go, 'forward'), 0.002)

	def pour_out(self):
		self.event = Clock.schedule_interval(partial(PumpMotor.pump_go, 'backward'), 0.002)

	def pour_stop(self):
		self.event.cancel()
		self.event = Clock.schedule_once(partial(PumpMotor.pump_stop), 0.01)

	async def start_scale(self, scale, ti):
		i = 0
		long = 10
		while long < i:
			sample = Scale.readCount()
			time.sleep(0.1)
			i++
			w = (scale - sample)/106
			self.ids.scale_value.text = str(round(w))
			time.sleep(0.1)
			await asyncio.sleep(1)