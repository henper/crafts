#!/usr/bin/env python3
import os, time
from phue import Bridge as PhilipsHueBridge

# Connect to Philips Hue Bridge
hue = PhilipsHueBridge()
hue.connect()

# state
monitorOn = True
brightness = 0

# shell commands for Rpi to enable and disable video output
videoOn  = 'ddcutil setvcp D6 01 --noverify'
videoOff = 'ddcutil setvcp D6 05 --noverify'

# shell commands for Rpi to adjust brightness with i2c over HDMI
setBrightness = 'ddcutil setvcp 10 '

# assume x86 for host, and arm for Pi. This won't hold forever :)
if os.uname()[4].startswith('x86'):
    videoOn  = 'echo "Display On"'
    videoOff = 'echo "Display Off"'
    setBrightness = 'echo "Adjusting brightness"'

def adjustBrightness():
    global brightness

    # Simple linear ambient to brightness, max brightness at 20000, min at 0.
    ambient = hue.get_sensor(sensor_id=7, parameter='state')['lightlevel']
    k = 200
    setpoint = min(100, int(ambient/k))

    if setpoint != brightness:
        brightness = setpoint
        os.system(setBrightness + str(brightness) + ' --noverify') # saw an error regarding max retries, author suggested no verify (used to be default)
        os.system('echo "Ambient at ' + str(ambient) + ' Brightness set to: ' + str(brightness) + '"') # log to stdout

def main():
    global monitorOn, host

    while(True):
        # Ids 6 = motion sensor, 7 = ambient light, 8 = temperature
        presence = hue.get_sensor(sensor_id=6, parameter='state')['presence']

        if monitorOn is not presence:
            # change state
            monitorOn = presence

            if monitorOn:
                os.system(videoOn)
            else:
                os.system(videoOff)

        if monitorOn:
            adjustBrightness()
            time.sleep(8)
        else:
            time.sleep(2)


if __name__ == "__main__":
    main()