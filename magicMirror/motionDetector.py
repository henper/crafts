#!/usr/bin/env python3
import os, sys, time
from phue import Bridge as PhilipsHueBridge

# Connect to Philips Hue Bridge
hue = PhilipsHueBridge()
hue.connect()

# state
monitorOn = True
brightness = 0
subsequent = 0

# shell commands for Rpi to enable and disable video output
#videoOn  = 'ddcutil setvcp D6 01 --noverify'
#videoOff = 'ddcutil setvcp D6 05 --noverify'
videoOn  = 'vcgencmd display_power 1; echo "Display On"'
videoOff = 'vcgencmd display_power 0; echo "Display Off"'

# shell commands for Rpi to adjust brightness with i2c over HDMI
setBrightness = 'ddcutil setvcp 10 '

# assume x86 for host, and arm for Pi. This won't hold forever :)
if os.uname()[4].startswith('x86'):
    videoOn  = 'echo "Display On"'
    videoOff = 'echo "Display Off"'
    setBrightness = 'echo "Adjusting brightness"'

def adjustBrightness(ambient):
    global brightness

    # Simple linear ambient to brightness, max brightness at 20000, min at 0.
    #ambient = hue.get_sensor(sensor_id=7, parameter='state')['lightlevel']
    k = 200
    setpoint = min(100, int(ambient/k))

    if setpoint != brightness:
        brightness = setpoint
        os.system(setBrightness + str(brightness) + ' --noverify') # saw an error regarding max retries, author suggested no verify (used to be default)
        os.system('echo "Ambient at ' + str(ambient) + ' Brightness set to: ' + str(brightness) + '"') # log to stdout

def onState():
    os.system(videoOn)

    subsequentNoPrescenceMeasurements = 0

    while subsequentNoPrescenceMeasurements < 12:
        try:
            sensors = hue.get_sensor() # get all sensors
            presence = sensors['6']['state']['presence']
            ambient = sensors['7']['state']['lightlevel']

            adjustBrightness(ambient) # continously adjust brightness when in on-state

            if not presence:
                subsequentNoPrescenceMeasurements += 1
                os.system(f'echo "no prescence detected, consecutive measurements: {subsequentNoPrescenceMeasurements}"')
            else:
                subsequentNoPrescenceMeasurements = 0
        except IOError as e:
            if e.errno == 101:
                sys.stderr.write('Network unreachable, retrying in 10 seconds.')
        except:
            raise

        time.sleep(10) # on period 8 seconds

def offState():
    os.system(videoOff)

    try:
        while not hue.get_sensor(sensor_id=6, parameter='state')['presence']:
            time.sleep(2) # off period 2 secs
    except IOError as e:
        if e.errno == 101:
            sys.stderr.write('Network unreachable, leaving off state.')
    except:
        raise

def main():
    os.system('echo "Motion detector initializing..."')

    try:

        while(True):
            onState()
            offState()
    except KeyboardInterrupt:
        os.system('echo "Performing proper shutdown..."')
        os.system(videoOn)

if __name__ == "__main__":
    main()