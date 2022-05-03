import RPi.GPIO as gpio
import Moduls.GlobalValues as GlobalValues
import time
from threading import Thread
import threading
import multiprocessing
import psutil
import asyncio

direct = GlobalValues.VMD
step = GlobalValues.VMS

import configparser
config = configparser.ConfigParser()
config.read('printer.ini')
vat_speed = float(config['DEFAULT']['vat_speed'])

direction = True

stop = False

class VatMotor():
    #queue = multiprocessing.Queue()
    async def stepper_go(speed, direction):
        #StepCounter = 0
        gpio.output(direct, direction)

        name = multiprocessing.current_process().name
        print(name, 'Starting')
        
        global _STOP
        _STOP = False
        
        while True:
            #stop = VatMotor.queue.get()
            #print(VatMotor.queue)
            #print(VatMotor.queue.get())
            if _STOP == True:
                break
            #turning the gpio on and off tells the easy driver to take one step
            gpio.output(step, True)
            time.sleep(speed)
            gpio.output(step, False)
        
            #Wait before taking the next step...this controls rotation speed
            time.sleep(speed)

    def stop_moving():
        print("Start stopping")
        for proc in psutil.process_iter():
            # check whether the process name matches
            print(proc.name())
            if proc.name() == 'VatSpin':
                proc.kill()

    def go():
        # moving = Thread(target=VatMotor.stepper_go, args=(vat_speed, direction))
        #moving = multiprocessing.Process(name='VatSpin', target=VatMotor.stepper_go, args=(vat_speed, direction))
        #moving.start()
        # moving.join()

        asyncio.run(VatMotor.stepper_go(vat_speed, direction))

        n_thread =  threading.active_count()
        print(n_thread)
