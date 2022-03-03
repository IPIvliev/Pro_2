import GlobalValues

test = GlobalValues.TEST
led_port = GlobalValues.LED_PORT

if test == 0:
  import RPi.GPIO as GPIO

class LED():
  if test == 0:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_port, GPIO.OUT)

	def turn_led_on():
    if test == 0:
		  GPIO.output(led_port, True)
    else:
      pass

	def turn_led_off():
		if test == 0:
      GPIO.output(led_port, False)
    else:
      pass