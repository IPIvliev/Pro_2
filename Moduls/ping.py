import urllib3
from kivy.clock import Clock
from functools import partial

class Ping():

	# Выводим статус подключения к сети на главной странице и странице Настроек
	def getPing(self, ti):
		try:
		    http=urllib3.PoolManager()
		    response = http.request('GET', 'http://google.com')
		    self.screens[0].ids.net_label.text = 'Online'
		    self.screens[3].ids.net_bottom.text = 'Online'
		    
		except:
			self.screens[0].ids.net_label.text = 'Offline'
			self.screens[3].ids.net_bottom.text = 'Offline'

	def callPing(self):
		Clock.schedule_interval(partial(Ping.getPing, self), 15)