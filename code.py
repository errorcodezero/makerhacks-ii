from microcontroller import Pin
from digitalio import DigitalInOut, Direction
import digitalio
import time
import board

# GP16 - b1
# GP17 - g1
# GP18 - r1

# GP19 - b2
# GP20 - g2
# GP21 - r2


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


def setup():
    RGBLed1 = RGBLed(board.GP18, board.GP17, board.GP16)
    RGBLed2 = RGBLed(board.GP21, board.GP20, board.GP19)
    RGBLed3 = RGBLed(board.GP26, board.GP27, board.GP22)
    RGBLed4 = RGBLed(board.GP14, board.GP13, board.GP15)

    RGBLed1.write_rgb(True, True, True)
    RGBLed2.write_rgb(True, True, True)
    RGBLed3.write_rgb(True, True, True)
    RGBLed4.write_rgb(True, True, True)

    return RGBLed1, RGBLed2, RGBLed3, RGBLed4

def main(l1: RGBLed, l2: RGBLed, l3: RGBLed, l4: RGBLed):
    time.sleep(2)

    l1.write_rgb(False, False, False)
    l2.write_rgb(False, False, False)
    l3.write_rgb(False, False, False)
    l4.write_rgb(False, False, False)
    time.sleep(0.5)

    while(True):
        l1.write_rgb(False, False, False)
        l2.write_rgb(False, False, False)
        l3.write_rgb(False, False, False)
        l4.write_rgb(False, False, False)
        time.sleep(0.5)

        l1.write_rgb(False, False, False)
        l2.write_rgb(False, False, False)
        l3.write_rgb(False, False, False)
        l4.write_rgb(False, False, False)
        time.sleep(0.5)



if __name__ == "__main__":
    l1, l2, l3, l4 = setup()
    main(l1, l2, l3, l4)