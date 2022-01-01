#!/usr/bin/env python3
import os, sys, asyncio
from phue import Bridge as PhilipsHueBridge
from phue import PhueRequestTimeout

# Connect to Philips Hue Bridge
hue = PhilipsHueBridge()
hue.connect()

# settings
OFF_STATE_MEAS_PERIOD = 2 # seconds
ON_STATE_MEAS_PERIOD = 10 # seconds
ON_STATE_SUBSEQUENT_PERIODS_WITH_NO_PRESCENCE = 12 # 2 minutes on time minimum
SLEW_RATE = 0.5 # 1 percent brightness change per 0.5 seconds

# state
monitorOn = True
brightness = 0

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
    setBrightness = 'echo "Adjusting brightness "'

async def adjustBrightness(ambient, slew = True):
    global brightness

    # Simple linear ambient to brightness, max brightness at 20000, min at 0.
    k = 200
    setpoint = min(100, int(ambient/k))

    step = 1
    if setpoint < brightness :
        step = -1
    if not slew:
        step = setpoint - brightness

    while brightness != setpoint:
        brightness += step

        os.system(setBrightness + str(brightness) + ' --noverify') # saw an error regarding max retries, author suggested no verify (used to be default)
        os.system('echo "Ambient at ' + str(ambient) + ' Brightness set to: ' + str(brightness) + '"') # log to stdout

        await asyncio.sleep(SLEW_RATE)

async def onState():
    os.system(videoOn)

    subsequentNoPrescenceMeasurements = 0

    while subsequentNoPrescenceMeasurements < ON_STATE_SUBSEQUENT_PERIODS_WITH_NO_PRESCENCE:
        try:
            sensors = hue.get_sensor() # get all sensors
            presence = sensors['6']['state']['presence']
            ambient = sensors['7']['state']['lightlevel']

            await adjustBrightness(ambient) # continously adjust brightness when in on-state

            if not presence:
                subsequentNoPrescenceMeasurements += 1
                os.system(f'echo "no prescence detected, consecutive measurements: {subsequentNoPrescenceMeasurements}"')
            else:
                subsequentNoPrescenceMeasurements = 0
        except IOError as e:
            if e.errno == 101:
                sys.stderr.write('Network unreachable, retrying in 10 seconds.')
        except PhueRequestTimeout:
            sys.stderr.write('Phue GET reqeust timed out, retrying...')
        except:
            raise

        await asyncio.sleep(ON_STATE_MEAS_PERIOD)

async def offState():
    os.system(videoOff)

    try:
        while not hue.get_sensor(sensor_id=6, parameter='state')['presence']:
            await asyncio.sleep(OFF_STATE_MEAS_PERIOD) # off period 2 secs
    except IOError as e:
        if e.errno == 101:
            sys.stderr.write('Network unreachable, leaving off state.')
    except PhueRequestTimeout:
            sys.stderr.write('Phue GET reqeust timed out, retrying...')
    except:
        raise

async def main():
    os.system('echo "Motion detector initializing..."')

    await adjustBrightness(10000, slew=False) # immideately set brightness to proper level

    try:
        while(True):
            await onState()
            await offState()
    except KeyboardInterrupt:
        os.system('echo "Performing proper shutdown..."')
        os.system(videoOn)

if __name__ == "__main__":
    asyncio.run(main())