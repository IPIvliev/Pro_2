import RPi.GPIO as GPIO

import configparser
config = configparser.ConfigParser()
config.read('printer_config.ini')
led_light = int(config.get("PORTS", "ledPort"))

class LED():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(led_light, GPIO.OUT)

	def turn_led_on():
		GPIO.output(led_light, True)

	def turn_led_off():
		GPIO.output(led_light, False)