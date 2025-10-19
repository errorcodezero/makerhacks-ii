from microcontroller import Pin
from digitalio import DigitalInOut, Direction
import digitalio
import time
import board
import pwmio
from adafruit_motor import servo

# GP16 - b1
# GP17 - g1
# GP18 - r1

# GP19 - b2
# GP20 - g2
# GP21 - r2

"""
Servos:
GP0 - servo 1
GP1 - servo 2
"""


servo_pwm_1 = pwmio.PWMOut(board.GP0, duty_cycle=2**15, frequency=50)

# Create a servo object, my_servo.
servo_1 = servo.Servo(servo_pwm_1)


servo_pwm_2 = pwmio.PWMOut(board.GP1, duty_cycle=2**15, frequency=50)

# Create a servo object, my_servo.
servo_2 = servo.Servo(servo_pwm_2)


class RGBLed:
    def __init__(self, r_pin: Pin, g_pin: Pin, b_pin: Pin):
        self.r_pin = DigitalInOut(r_pin)
        self.g_pin = DigitalInOut(g_pin)
        self.b_pin = DigitalInOut(b_pin)

        self.r_pin.direction = Direction.OUTPUT
        self.g_pin.direction = Direction.OUTPUT
        self.b_pin.direction = Direction.OUTPUT

    def write_r(self, value: bool):
        self.r_pin.value = value

    def write_g(self, value: bool):
        self.g_pin.value = value

    def write_b(self, value: bool):
        self.b_pin.value = value

    def write_rgb(self, r_value: bool, g_value: bool, b_value: bool):
        self.write_r(r_value)
        self.write_g(g_value)
        self.write_b(b_value)


def main():
    time.sleep(2)

    l1 = RGBLed(board.GP18, board.GP17, board.GP16)
    l2 = RGBLed(board.GP21, board.GP20, board.GP19)
    l3 = RGBLed(board.GP26, board.GP27, board.GP22)
    l4 = RGBLed(board.GP14, board.GP13, board.GP15)

    l1.write_rgb(False, False, False)
    l2.write_rgb(False, False, False)
    l3.write_rgb(False, False, False)
    l4.write_rgb(False, False, False)
    time.sleep(0.5)
<<<<<<< Updated upstream

    while (True):
=======
    angle = 90
    while True:
>>>>>>> Stashed changes
        l1.write_rgb(False, False, False)
        l2.write_rgb(False, False, False)
        l3.write_rgb(False, False, False)
        l4.write_rgb(False, False, False)
        servo_1.angle = angle
        servo_2.angle = angle
        angle = 0
        time.sleep(0.5)

        l1.write_rgb(False, False, False)
        l2.write_rgb(False, False, False)
        l3.write_rgb(False, False, False)
        l4.write_rgb(False, False, False)
        servo_1.angle = angle
        servo_2.angle = angle
        angle = 90
        time.sleep(0.5)


if __name__ == "__main__":
    main()
