#!/usr/bin/env python

## Servo Controller
# By default, this is not used. Enable if your project needs it.
# Modified by Anton
# Original Simon Monk @Adafruit

import time
import wiringpi
 
def open_door(wiringpi, delay_period):
    for pulse in range(50, 250, 1):
        wiringpi.pwmWrite(18, pulse)
        time.sleep(delay_period)

def close_lock(wiringpi, delay_period):
    for pulse in range(250, 50, -1):
        wiringpi.pwmWrite(18, pulse)
        time.sleep(delay_period)

if __name__ == '__main__':
    # use 'GPIO naming'
    wiringpi.wiringPiSetupGpio()

    # set #18 to be a PWM output
    wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

    # set the PWM mode to milliseconds stype
    wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

    # divide down clock
    wiringpi.pwmSetClock(192)
    wiringpi.pwmSetRange(2000)

    delay_period = 0.01
