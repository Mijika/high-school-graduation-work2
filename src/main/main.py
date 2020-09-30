import os
from time import sleep

from utils.custom_logger import Logger
from servo_controller import ServoMotortController

logger = Logger(__name__)


def main():
    sleep(1)
    servo_controller = ServoMotortController()
    servo_controller.setup_servo_moter()
    servo_controller.setServoPos(100)

    try:
        while True:
            pass

    except KeyboardInterrupt:
        logger.info(' program close')

if __name__ == '__main__':
    main()
