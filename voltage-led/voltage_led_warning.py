#!/usr/bin/env python3

import time

VOLTAGE_PATH = "/sys/class/power_supply/battery/voltage_now"
RED_LED = "/sys/devices/platform/arkos4clone-leds/leds/led-red/brightness"
BLUE_LED = "/sys/devices/platform/arkos4clone-leds/leds/led-blue/brightness"

DEFAULT_CRITICAL = 3000000
DEFAULT_LOW = 3200000

def load_config():
    critical = DEFAULT_CRITICAL
    low = DEFAULT_LOW
    return critical, low

def set_led(path, value):
    with open(path, "w") as f:
        f.write(str(value))

def read_led(path):
    with open(path) as f:
        return int(f.read().strip())

critical, low = load_config()

while True:
    voltage = int(open(VOLTAGE_PATH).read().strip())
    if voltage <= critical:
        set_led(BLUE_LED, 0)
        set_led(RED_LED, 0 if read_led(RED_LED) else 1)
    elif voltage <= low:
        set_led(BLUE_LED, 0)
        set_led(RED_LED, 1)
    else:
        set_led(RED_LED, 0)
        set_led(BLUE_LED, 0)

    time.sleep(5)