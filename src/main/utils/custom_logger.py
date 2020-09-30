import logging

from config import *


class Logger:
    """Custom logging class

    It is a lapping of the logging class.
    """

    def __init__(self, name):
        """Create Logger Object

        Receive name Arguments to create a logger

        Arguments:
            name {str} -- Name of the logger object
        """

        self.logger = logging.getLogger(class_name)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stream_hander = logging.StreamHandler()
        stream_hander.setFormatter(formatter)
        self.logger.addHandler(stream_hander)

        if PROGRAM_STATUS == DEVELOPMENT:
            self.logger.setLevel(logging.DEBUG)
        elif ROGRAM_STATUS == RUN:
            self.logger.setLevel(logging.WARNING)

    def debug(self, log):
        """ debug

        debug wrapping on logging module

        Arguments:
            log {str} -- log message
        """

        self.logger.debug(log)

    def info(self, log):
        """ info

        info wrapping on logging module

        Arguments:
            log {str} -- log message
        """

        self.logger.info(log)

    def warning(self, log):
        """ warning

        warning wrapping on logging module

        Arguments:
            log {str} -- log message
        """

        self.logger.warning(log)

    def error(self, log):
        """ error

        error wrapping on logging module

        Arguments:
            log {str} -- log message
        """

        self.logger.error(log)

    def critical(self, log):
        """ critical

        critical wrapping on logging module

        Arguments:
            log {str} -- log message
        """

        self.logger.critical(log)

