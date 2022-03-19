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
        GPIO.output(Standby, True)
        print("motorone set")
        GPIO.output(AI1, True)
        GPIO.output(AI2, False)
        time.sleep(2)
        print("motor test")
        GPIO.output(PWA, True)
        time.sleep(5)
    finally:
        GPIO.output(Standby, False)
        GPIO.cleanup()

    exit()


# =====================END===============================