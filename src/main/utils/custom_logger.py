import logging

from config import *


class Logger:
    def __init__(self, class_name):
        self.logger = logging.getLogger(class_name)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stream_hander = logging.StreamHandler()
        stream_hander.setFormatter(formatter)
        self.logger.addHandler(stream_hander)

        if PROGRAM_STATUS == DEVELOPMENT:
            self.logger.setLevel(logging.DEBUG)
        elif ROGRAM_STATUS == RUN:
            self.logger.setLevel(logging.WARNING)

    def info(self, log):
        self.logger.info(log)
