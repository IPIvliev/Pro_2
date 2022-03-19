import RPi.GPIO as GPIO

TEST = 0 # Работает в тестовом режиме без GPIO
LED_PORT = 18 # Порт для освещение принтера
LIGHT_PORT = 22 # Порт для управления LED-матрицей
# Насос фотополмера
PUMPPOWERPORT = 26 # Сигнал в работу
PUMPAI1 = 13 # Сигнал на движение по часовой
PUMPAI2 = 19 # Сигнал на движение против часовой
PUMPSTANDBY = 6 # Сигнал готовности к движению
# Датчики веса
DT = 27
SCK = 17
# Шаговый двигатель по оси Z
ZMD = 16 # Сигнал направления
ZMS = 20 # Сигнал движения на шаг
# Шаговый двигатель привода ванны
VMD = 22 # Сигнал направления
VMS = 23 # Сигнал движения на шаг

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PORT, GPIO.OUT)
GPIO.setup(LIGHT_PORT, GPIO.OUT)
GPIO.setup(SCK, gpio.OUT)
GPIO.setup(ZMD, gpio.OUT)
GPIO.setup(ZMS, gpio.OUT)
GPIO.setup(VMS, gpio.OUT)
GPIO.setup(VMD, gpio.OUT)