from kivy.uix.screenmanager import Screen
from Moduls.stepper import Motor
from Moduls.stepper1 import Motor1
from kivy.clock import Clock
from functools import partial
import threading

distance = 10
format_of_go = True

class ZMovingWindow(Screen):


	def go_10(self):
		global distance
		distance = 8
		print(distance)

	def go_50(self):
		global distance
		distance = 40
		print(distance)

	def go_100(self):
		global distance
		distance = 80
		print(distance)

	def go_1000(self):
		global distance
		distance = 800
		print(distance)

	def by_step(self):
		global format_of_go
		format_of_go = True
		
	def by_distance(self):
		global format_of_go
		format_of_go = False		

	def motor_go_up(self):
		print('UP')
		if format_of_go == True:
			Clock.schedule_once(partial(ZMovingWindow.motor_go, self, distance, False), 0.1)
		else:
			Clock.schedule_once(partial(ZMovingWindow.motor1_go, self, 9999999, False), 0.1)
			
	def motor_go_down(self):
		print('Down')
		if format_of_go == True:
			Clock.schedule_once(partial(ZMovingWindow.motor_go, self, distance, True), 0.1)
		else:
			Clock.schedule_once(partial(ZMovingWindow.motor1_go, self, 9999999, True), 0.1)

	def stop(self):
		Motor1.stop_moving()

	def motor_go(self, distance, direction, ti):
		Motor.stepper_go(0.0001, distance, direction)
	def motor1_go(self, distance, direction, ti):
		printing = threading.Thread(target=Motor1.stepper_go, args=(self, 0.00001, distance, direction))
		printing.daemon = True
		printing.start()		
