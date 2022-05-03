import RPi.GPIO as gpio
import Moduls.GlobalValues as GlobalValues
import time
from threading import Thread
import threading
import multiprocessing

direct = GlobalValues.VMD
step = GlobalValues.VMS

direction = True

stop = False

class VatMotor():
    #queue = multiprocessing.Queue()
    def stepper_go(speed, direction):
        #StepCounter = 0
        gpio.output(direct, direction)
        
        global stop
        stop = False
        
        while True:
            #stop = VatMotor.queue.get()
            #print(VatMotor.queue)
            #print(VatMotor.queue.get())
            if stop == True:
                break
            #turning the gpio on and off tells the easy driver to take one step
            gpio.output(step, True)
            time.sleep(speed)
            gpio.output(step, False)
        
            #Wait before taking the next step...this controls rotation speed
            time.sleep(speed)

    def stop_moving():
        global stop
        stop = True
        #VatMotor.queue.put(stop)

    def go():
        # moving = multiprocessing.Process(target=VatMotor.stepper_go, args=(vat_speed, direction))
        moving = Thread(target=VatMotor.stepper_go, args=(0.0001, direction))
        moving.start()
        # moving.join()
        n_thread =  threading.active_count()
        print(n_thread)
