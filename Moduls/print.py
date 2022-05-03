import os, shutil, time, subprocess
from pyphotonfile import Photon
from multiprocessing import Pool
from kivy.clock import Clock
from functools import partial
from Screens.PrintProcessWindow._popup_finish_printing import PopupFinishPrinting
from kivy.properties import BooleanProperty
from Moduls.stepper import Motor
from Moduls.stepper1 import Motor1
from Moduls.vat_stepper import VatMotor
from Moduls.led import LED
from Moduls.scale import Scale

pause = BooleanProperty()
pause = False
stop = BooleanProperty()
stop = False

# Получаем параметры работы швп по Z
import configparser
config = configparser.ConfigParser()
config.read('printer_config.ini')

class Print():
	z_step_mm = 0.00125 # Сколько мм в 1 шаге ШПВ
	vat_delay = 0.5 # Задержка выключения поворота ванны после окончания подъёма по оси Z
#	vat_z_delay = config.get("DEFAULT", "vat_z_delay") # Задержка между началом поворота ванны и началом подъёма платформы
	vat_z_delay = 0.5 # Задержка между началом поворота ванны и началом подъёма платформы

	def unzip(photon):
		pool = Pool(3)
		x = ['Temp']
		pool.map(photon.export_images, x)
		pool.close()
		pool.join()		

	def clear_temp():
		folder = 'Temp'
		for filename in os.listdir(folder):
		    file_path = os.path.join(folder, filename)
		    try:
		        if os.path.isfile(file_path) or os.path.islink(file_path):
		            os.unlink(file_path)
		        elif os.path.isdir(file_path):
		            shutil.rmtree(file_path)
		    except Exception as e:
		        print('Failed to delete %s. Reason: %s' % (file_path, e))

#	async def printing(self):
	def printing(self, photon):
		#  Определяем параметры печати
		z_step_amount = round(photon.layer_height, 2) / float(Print.z_step_mm)
		exposure_time = float(photon.exposure_time)
		vat_delay = float(Print.vat_delay)
		vat_z_delay = float(Print.vat_z_delay)
		layer_height = round(photon.layer_height, 2)
		layer_thinkness = int(layer_height)

		global pause
		pause = False
		global stop
		stop = False

		temp_dir = 'Temp'
		dir = os.listdir(temp_dir)
		self.manager.screens[9].ids.layer_img.source = 'Static/Images/black.png'

		# Подготавливаем печатную платформу. Проверяем парарельность, идём вниз до ванны
		Print.prepearing_for_printing(self, layer_thinkness)

		# Экспонируем слои на дисплей
		with os.scandir(temp_dir) as files:
			for layer in files:
				if stop == True:
					break

				while pause == True:
					time.sleep(2)

				# Выводим текущий слой на LCD дисплей
				Clock.schedule_once(partial(Print.setLayerImage, self, layer), 1)
				l = subprocess.Popen(['python3', 'two.py', layer], stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=False)
				print('Выводим слой', layer.name, 'на LCD дисплей')

				# Включаем LED матрицу на время, указанное параметрах модели и выключаем
				Print().turn_led(exposure_time)

				# Выключаем вывод текущего слоя на LCD дисплей
				l.terminate()

				# Включаем поворот ванны и парарельно перемещаемся вверх по z
				Print().vat_and_z_go(vat_delay, vat_z_delay, z_step_amount)

		self.manager.screens[9].ids.layer_img.source = 'Static/Images/black.png'

		# После окончания печати двигаем платформу вверх до заданного значения (в шагах)
		Print().after_printing(1000)

		if stop == False:
			PopupFinishPrinting.show_popup()

	def setLayerImage(self, layer, time):
		self.manager.screens[9].ids.layer_img.source = 'Temp/' + layer.name

	def stop_printing():
		Print.clear_temp()
		global stop
		stop = True

	def pause_printing():
		global pause
		pause = not pause

	def prepearing_for_printing(self, layer_thinkness):
		print('Проверяем парарельность печатающей платформы. Если в допусках, то начинаем печать')

		print('Проверяем наличие полимера в ванной. Если достоточно, начинаем печать, иначе доливаем')
		#Distance.check_distance()

		print('Z идёт вниз до срабатывания тензо датчика')
		Print.z_go_stepper1(self, 400)
		print('Z останавливается')

		# Перемещаем платформу на толщину слоя для начала печати первого слоя
		print('Z перемещается на n микронн вверх')
		Print.z_go_stepper(layer_thinkness)

	def turn_led(self, exposure_time):
		# Включаем светодиодную матрицу
		print('LED включены')
		LED.turn_led_on()

		# Устанавливаем время горение матрицы - exposure_time
		print('Задержка выключения LED', exposure_time, 'секунд')
		time.sleep(exposure_time)

		LED.turn_led_off()
		print('LED выключены')

	def vat_and_z_go(self, vat_delay, vat_z_delay, layer_thinkness):
		
		print('Проверяем наличие полимера в ванной. Если достоточно, начинаем печать, иначе доливаем')
		#Distance.check_distance()

		# Включаем поворот ванны
		print('Включаем поворот ванны')
		VatMotor.go()


		# Включаем задержку между началом поворота ванны и началом подъёма платформы
		print('Задержка в размере', vat_z_delay, 'до подъёма платформы')
		time.sleep(vat_z_delay)

		# Двигаемся вверх на толщину слоя
		Print.z_go_stepper(layer_thinkness)

		# vat_delay - сколько времени ванна продолжит крутиться, после окончания подъёма платформы на толщину layer_thinkness
		time.sleep(vat_delay)
		VatMotor.stop_moving()
		print('Выключаем поворот ванны после задержки в', vat_delay, 'секунды')

	def z_go_stepper(z_layer):
		print('Z перемещается вверх на', int(z_layer), 'шагов')
		Motor.stepper_go(0.00001, int(z_layer), False)

	def z_go_stepper1(self, z_layer):
		print('Z перемещается вверх на', int(z_layer), 'шагов')
		Motor1.stepper_go(self, 0.00001, int(z_layer), False)

	def after_printing(self, z_height):
		print('Двигаем печатную платформу вверх на', z_height, 'шагов')
