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
	def __init__(self):
		self.servo1 = None
		self.servo2 = None

	def __del__(self):
		if isinstance(self.servo1, GPIO.PWM):
			self.servo1.stop()
			self.servo2.stop()

		GPIO.cleanup()

	def setup_servo_moter(self):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False) # gpio warning disable

		GPIO.setup(SERVO_MOTOR1_PIN, GPIO.OUT)
		GPIO.setup(SERVO_MOTOR2_PIN, GPIO.OUT)

		self.servo1 = GPIO.PWM(SERVO_MOTOR1_PIN, 50)
		self.servo2 = GPIO.PWM(SERVO_MOTOR2_PIN, 50)

		self.servo1.start(0)
		self.servo2.start(0)

	def setServoPos(self, degree):
		# 각도는 180도를 넘을 수 없다.
		if degree > 180:
			degree = 180

		# 각도(degree)를 duty로 변경한다.
		duty = SERVO_MIN_DUTY+(degree*(SERVO_MAX_DUTY-SERVO_MIN_DUTY)/180.0)
		# duty 값 출력
		logger.info("Degree: {} to {}(Duty)".format(degree, duty))

		# 변경된 duty값을 서보 pwm에 적용
		self.servo1.ChangeDutyCycle(duty)
		self.servo2.ChangeDutyCycle(duty)


if __name__ == '__main__':
	servo_controller = ServoMotortController()
	servo_controller.setup_servo_moter()
	servo_controller.setServoPos(100)
