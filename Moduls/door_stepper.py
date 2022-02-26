import RPi.GPIO as gpio
import time
from threading import Thread

import configparser
config = configparser.ConfigParser()
config.read('printer_config.ini')

step = 23
direct = 24

# Устанавливаем пин концевика
limit_switcher_open = 13
limit_switcher_close = 12

door_speed = float(config['DEFAULT']['door_speed'])
distance=500000

stop = False

class DoorMotor():
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(limit_switcher_open, gpio.IN) 
    gpio.setup(limit_switcher_close, gpio.IN) 
    
    def stepper_go(door_speed, distance, direction, action):
        
        gpio.setup(step, gpio.OUT)
        gpio.setup(direct, gpio.OUT)

        # Устанавливаем пин оптического концевика на вход

        StepCounter = 0

        # Определяем направление движения
        gpio.output(direct, direction)
        
        global stop
        stop = False
        
        while StepCounter < distance:
            
            switcher_status_open = gpio.input(limit_switcher_open)
            switcher_status_close = gpio.input(limit_switcher_close)
            
            if action == 'close' and switcher_status_close == False:
                break
            if action == 'open' and switcher_status_open == False:
                break
            #turning the gpio on and off tells the easy driver to take one step
            gpio.output(step, True)
            time.sleep(door_speed)
            gpio.output(step, False)
            StepCounter += 1
            WaitTimeAccel = door_speed
         
            #Wait before taking the next step...this controls rotation speed
            time.sleep(WaitTimeAccel)

    def stop_moving():
        global stop
        stop = True

    def go():
        switcher_status_open = gpio.input(limit_switcher_open)
        switcher_status_close = gpio.input(limit_switcher_close)
        
        direction = True
        action = 'close'
        
        if switcher_status_open == False and switcher_status_close == True:
            direction = True
            action = 'close'
        elif switcher_status_open == True and switcher_status_close == False:
            direction = False
            action = 'open'
            
        moving = Thread(target=DoorMotor.stepper_go, args=(door_speed, distance, direction, action))
        moving.daemon = True
        moving.start()
