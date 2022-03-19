import RPi.GPIO as GPIO
import time
import Moduls.GlobalValues as GlobalValues

DT = GlobalValues.DT
SCK = GlobalValues.SCK

stop = False

class Scale():

  def readCount():
    GPIO.setup(SCK, GPIO.OUT)
    i=0
    Count=0
    GPIO.setup(DT, GPIO.OUT)
    GPIO.output(DT,1)
    GPIO.output(SCK,0)
    GPIO.setup(DT, GPIO.IN)

    while GPIO.input(DT) == 1:
        i=0
    for i in range(24):
            
          GPIO.output(SCK,1)
          Count=Count<<1

          GPIO.output(SCK,0)
          time.sleep(0.01)
          if GPIO.input(DT) == 0: 
              Count=Count+1
          
    GPIO.output(SCK,1)
    Count=Count^0x800000
    GPIO.output(SCK,0)
    return Count

  def scale_stop():
    GPIO.cleanup([27, 17])

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
