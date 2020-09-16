import time
import os
import platform

import utils.custom_logger


DEVELOPMENT = 0  # 개발 중일때 사용
RUN = 10 # 개발 끝나고 사용

if platform.system() == "Windows":
	DEIVER_PATH = './chromedriver.exe'
elif platform.system() == "Linux":
	import RPi.GPIO as GPIO



def is_system_on():


while True():

	time.slepp(0.1)




if __name__ == "__main__":
	pass


import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(6, GPIO.OUT)
GPIO.setup(21, GPIO.IN)

try:
    while True:
        inputIO = GPIO.input(21)

        if inputIO == False:
            GPIO.output(6, GPIO.HIGH)
            #time.sleep(1)

        else:
            GPIO.output(6, GPIO.LOW)
            #time.sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()