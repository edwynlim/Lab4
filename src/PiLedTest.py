import socket
import time
from time import sleep
from hal import hal_led as led
from hal import hal_input_switch as switch


def blink_led(delay):
    # Led Blink
    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)


def main():
    x = 0
    led.init()
    switch.init()

    while True:
        if switch.read_slide_switch() == 1:
            blink_led(0.2)
            x = 0

        else:
            # 25 x 0.2 = 5seconds
            while x < 26:
                blink_led(0.1)
                led.set_output(0, 0)
                x += 1


# Main entry point
if __name__ == "__main__":
    main()
