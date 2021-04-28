#!/usr/bin/env python3
import os, time
from phue import Bridge as PhilipsHueBridge

# Connect to Philips Hue Bridge
hue = PhilipsHueBridge()
hue.connect()

# state
monitorOn = True

# shell commands for Rpi to enable and disable video output
videoOn  = 'vcgencmd display_power 1; echo "Display On"'
videoOff = 'vcgencmd display_power 0; echo "Display Off"'

# assume x86 for host, and arm for Pi. This won't hold forever :)
if os.uname()[4].startswith('x86'):
    videoOn  = 'echo "Display On"'
    videoOff = 'echo "Display Off"'

def main():
    global monitorOn, host

    while(True):
        # Ids 6 = motion sensor, 7 = ambient light, 8 = temperature
        presence = hue.get_sensor(sensor_id=6, parameter='state')['presence']

        if monitorOn is not presence:
            # change state
            monitorOn = presence

            if monitorOn is True:
                os.system(videoOn)
            else:
                os.system(videoOff)

        if monitorOn:
            time.sleep(8)
        else:
            time.sleep(2)


if __name__ == "__main__":
    main()