import RPi.GPIO as gpio
import Moduls.GlobalValues as GlobalValues
import time
import threading
from Moduls.scale import Scale
import configparser
config = configparser.ConfigParser()
config.read('printer_config.ini')

motor_direction = GlobalValues.ZMD
step = GlobalValues.ZMS

stop = False

class Motor1():

    tenzor_weight = config.get("DEFAULT", "tenzo_weight")

    def stepper_go(self, speed, distance, direction):
        StepCounter = 0
        gpio.output(motor_direction, direction)
        
        global stop
        stop = False
        
        # Start tenzo to prevent damage
        print(distance)
        if distance != 400:
            scaling = threading.Thread(target=Motor1.start_scale, args=(self, 1))
            scaling.daemon = True
            scaling.start()
        
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

    # good practise to cleanup GPIO at some point before exit
        #gpio.cleanup()

    def stop_moving():
        global stop
        stop = True
        
    def start_scale(self, t):
        sample = Scale.readCount()
        weight = float(Motor1.tenzor_weight)
        
        while True:

            count = Scale.readCount()
            w=0
            w=(count-sample)/106
            self.ids.scale_value.text = str(round(w))
            
            if int(w) > weight:
              Motor1.stop_moving()
              Scale.scale_stop()
              break
            if stop == True:
              Scale.scale_stop()
              break
            time.sleep(0.3)
