import RPi.GPIO as gpio
import time
import threading
from Moduls.scale import Scale
import configparser
config = configparser.ConfigParser()
config.read('printer_config.ini')

stop = False
gpio.setmode(gpio.BCM)

class Motor1():

    tenzor_weight = config.get("DEFAULT", "tenzo_weight")

    def stepper_go(speed, distance, direction):
        gpio.setmode(gpio.BCM)

        gpio.setwarnings(False)
        gpio.setup(16, gpio.OUT)
        gpio.setup(20, gpio.OUT)
        StepCounter = 0
        gpio.output(16, direction)
        
        global stop
        stop = False
        
        # Start tenzo to prevent damage
        scaling = threading.Thread(target=Motor1.start_scale, args=( ))
        scaling.daemon = True
        scaling.start()	
        
        while StepCounter < distance:
            if stop == True:
                break
            #turning the gpio on and off tells the easy driver to take one step
            gpio.output(20, True)
            time.sleep(speed)
            gpio.output(20, False)
            StepCounter += 1
            WaitTimeAccel = speed
         
            #Wait before taking the next step...this controls rotation speed
            time.sleep(WaitTimeAccel)

    #mymotortest.motor_move(.005, 200 , False, True, "Full", .05)

    # good practise to cleanup GPIO at some point before exit
        #gpio.cleanup()

    def stop_moving():
        global stop
        stop = True
        
    def start_scale():
        sample = Scale.readCount()
        weight = float(Motor1.tenzor_weight)
        
        while True:

            count = Scale.readCount()
            w=0
            w=(count-sample)/106
            print(w)
            
            if int(w) > weight:
              Motor1.stop_moving()
              Scale.scale_stop()
              break
            if stop == True:
              Scale.scale_stop()
              break
            time.sleep(0.1)
