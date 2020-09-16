import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(
			os.path.abspath(os.path.dirname(
				os.path.abspath(os.path.dirname(__file__))))))

from main.utils.custom_logger import Logger

class LoggerTests(unittest.TestCase):
	def test_generating(self):
		""" 객체가 생성되는지 판별"""
		self.logger = Logger(__name__)



if __name__ == '__main__':
	unittest.main()
