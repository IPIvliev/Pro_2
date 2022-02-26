# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the VL53L0X distance sensor.
# Will print the sensed range/distance every second.
#import time

import board
import busio
from Moduls.pump_motor import PumpMotor

import adafruit_vl53l0x
# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

import configparser
config = configparser.ConfigParser()
config.read('printer_config.ini')


# Optionally adjust the measurement timing budget to change speed and accuracy.
# See the example here for more details:
#   https://github.com/pololu/vl53l0x-arduino/blob/master/examples/Single/Single.ino
# For example a higher speed but less accurate timing budget of 20ms:
# vl53.measurement_timing_budget = 20000
# Or a slower but more accurate timing budget of 200ms:
# vl53.measurement_timing_budget = 200000
# The default timing budget is 33ms, a good compromise of speed and accuracy.

# Устанавливаем расстояние до ванны и вычисляем процент заполнения ванны
vat_amount = config.get("DEFAULT", "vat_amount") # На сколько % заполнять ванну
min = 150
max = 180
average = max - min # 30
amount = average / 100 * int(vat_amount) # 15
normal = max - amount # 165

class Distance():
    def check_distance():
        distance = float(vl53.range)
        print('Distance: ', distance)
        if distance < float(normal):
            print("Range: {0}mm".format(vl53.range))
            PumpMotor.pump_go('forward', 3)

