from kivy.uix.screenmanager import Screen
from pyphotonfile import Photon
import time
from Moduls.print import Print
import threading

class PrintProcessWindow(Screen):


	def on_enter(self, *largs):
		pass

	def model_preparetion(self, filename):
     
		photon = Photon(filename[0])
		
		weight_g = int(photon.weight_g)
		layer_height = round(photon.layer_height, 2)
		lifting_speed = round(photon.lifting_speed, 2)
		print_time = time.strftime('%H:%M:%S', time.gmtime(photon.print_time))

		model_name = filename[0].rsplit('\\')
		self.ids.model_name.text = str(model_name[-1])
		self.ids.bottom_light.text = str(photon.exposure_time_bottom)
		self.ids.main_light.text = str(photon.exposure_time)
		self.ids.model_weight.text = str(weight_g)
		self.ids.model_thinkness.text = str(layer_height)
		self.ids.printing_time.text = str(print_time)
		self.ids.layers_amount.text = str(photon.n_layers)
		self.ids.lifting_speed.text = str(lifting_speed)

		# Разархивируем модель
		Print.unzip(photon)

		# Начинаем печать
		printing = threading.Thread(target=Print.printing, args=(self, photon))
		printing.daemon = True
		printing.start()

	def pause(self):
		Print.pause_printing()

	def stop(self):
		Print.stop_printing()
