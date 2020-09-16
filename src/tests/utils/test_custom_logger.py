import unittest
import sys


class LoggerTests(unittest.TestCase):
	def setUp(self):
		"""파일 링크"""
		sys.path.insert(0, "../../main")
		from utils.custom_logger import Logger


	def test_generating(self):
		""" 객체가 생성되는지 판변"""
		logger = Logger()

if __name__ == '__main__':
	unittest.main()