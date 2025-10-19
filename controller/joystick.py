import time
import board
import analogio

x = analogio.AnalogIn(board.GP28)
y = analogio.AnalogIn(board.GP27)
print("Beepbeep")


def get_voltage(raw):
    return (raw * 3.3) / 65536


while True:
    x_raw = x.value
    x_volts = get_voltage(x_raw)
    y_raw = y.value
    y_volts = get_voltage(y_raw)
    print(x_volts, y_volts)
    # print("x: raw = {:5d} volts = {:5.2f}, y: raw = {:5d} volts = {:5.2f}".format(x_raw, x_volts,y_raw, y_volts))
    time.sleep(0.1)
