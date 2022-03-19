import Moduls.GlobalValues as GlobalValues

test = GlobalValues.TEST
led_port = GlobalValues.LED_PORT

if test == 0:
  import RPi.GPIO as GPIO

class LED():

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