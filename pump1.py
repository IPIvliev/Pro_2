import RPi.GPIO as GPIO
import Moduls.GlobalValues as GlobalValues
import time

PWA = GlobalValues.PUMPPOWERPORT
AI1 = GlobalValues.PUMPAI1
AI2 = GlobalValues.PUMPAI1
Standby = GlobalValues.PUMPSTANDBY

# ===================MAIN===============================

if __name__ == '__main__':
    try:
        print("START")
        time.sleep(0.1)
        GPIO.output(Standby, True)
        time.sleep(0.1)
        print("motorone set")
        GPIO.output(AI1, True)
        GPIO.output(AI2, False)
        time.sleep(2)
        print("motor test")
        while True:
            GPIO.output(PWA, True)
            time.sleep(0.1)
            GPIO.output(PWA, False)
            time.sleep(0.1)
        time.sleep(20)
    finally:
        print("Stop test")
        GPIO.output(Standby, False)
        GPIO.cleanup()

    exit()


# =====================END===============================