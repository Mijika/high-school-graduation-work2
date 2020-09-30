import RPi.GPIO as GPIO
import logging

from utils.custom_logger import Logger


logger = Logger(__name__)

# servo motor pin allocation
SERVO_MOTOR1_PIN = 16
SERVO_MOTOR2_PIN = 18

# servo motor set duty
SERVO_MAX_DUTY = 12
SERVO_MIN_DUTY = 3

class ServoMotortController:
	"""Class controlling two servomotor

	"""
	def __init__(self):
		self.servo1 = None
		self.servo2 = None

	def __del__(self):
		if isinstance(self.servo1, GPIO.PWM):
			self.servo1.stop()
			self.servo2.stop()

		GPIO.cleanup()

	def setup_servo_moter(self):
		"""setup servo moter


		"""
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False) # gpio warning disable

		GPIO.setup(SERVO_MOTOR1_PIN, GPIO.OUT)
		GPIO.setup(SERVO_MOTOR2_PIN, GPIO.OUT)

		self.servo1 = GPIO.PWM(SERVO_MOTOR1_PIN, 50)
		self.servo2 = GPIO.PWM(SERVO_MOTOR2_PIN, 50)

		self.servo1.start(0)
		self.servo2.start(0)

	def setServoPos(self, degree):
		"""Specify angle of servomotor

		Arguments:
			degree {int} -- specify degree
		"""

		# cannot exceed 180 degrees.
		if degree > 180:
			degree = 180
		# cannot be less than 0 degrees.
		if degree < 0:
			degree = 0

		# change the degree to duty
		duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
		logger.debug("Degree: {} to {}(Duty)".format(degree, duty))

		# Apply Value
		self.servo1.ChangeDutyCycle(duty)
		self.servo2.ChangeDutyCycle(duty)


if __name__ == '__main__':
	servo_controller = ServoMotortController()
	servo_controller.setup_servo_moter()
	servo_controller.setServoPos(100)
