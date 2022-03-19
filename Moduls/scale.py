import RPi.GPIO as gpio
import time
import Moduls.GlobalValues as GlobalValues

DT = GlobalValues.DT
SCK = GlobalValues.SCK

stop = False

class Scale():

  def readCount():  
    i=0
    Count=0
    gpio.setup(DT, gpio.OUT)
    gpio.output(DT,1)
    gpio.output(SCK,0)
    gpio.setup(DT, gpio.IN)

    while gpio.input(DT) == 1:
        i=0
    for i in range(24):
            
          gpio.output(SCK,1)
          Count=Count<<1

          gpio.output(SCK,0)
          time.sleep(0.01)
          if gpio.input(DT) == 0: 
              Count=Count+1
          
    gpio.output(SCK,1)
    Count=Count^0x800000
    gpio.output(SCK,0)
    return Count

  def scale_stop():
    gpio.cleanup([27, 17])

  def start_scale():
    sample = Scale.readCount()
    while True:
      count = Scale.readCount()
      w=0
      w=(count-sample)/106
      if int(w) > int(100):
          Scale.scale_stop()
          break
      time.sleep(0.1)
#Scale.start_scale()
