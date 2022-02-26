import RPi.GPIO as gpio
import time
from threading import Thread

import configparser
config = configparser.ConfigParser()
config.read('printer_config.ini')

step = 23
direct = 22

vat_speed = float(config['DEFAULT']['vat_speed'])
distance = 9999
direction = True

stop = False
gpio.setmode(gpio.BCM)

class VatMotor():

    def stepper_go(speed, distance, direction):
        gpio.setmode(gpio.BCM)

        gpio.setwarnings(False)
        gpio.setup(step, gpio.OUT)
        gpio.setup(direct, gpio.OUT)
        StepCounter = 0
        gpio.output(direct, direction)
        
        global stop
        stop = False
        
        while StepCounter < distance:
            if stop == True:
                break
            #turning the gpio on and off tells the easy driver to take one step
            gpio.output(step, True)
            time.sleep(speed)
            gpio.output(step, False)
            StepCounter += 1
            WaitTimeAccel = speed
         
            #Wait before taking the next step...this controls rotation speed
            time.sleep(WaitTimeAccel)

    def stop_moving():
        global stop
        stop = True

    def go():
        moving = Thread(target=VatMotor.stepper_go, args=(vat_speed, distance, direction))
        moving.daemon = True
        moving.start()
