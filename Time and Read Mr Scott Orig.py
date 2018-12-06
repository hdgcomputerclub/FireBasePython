# Time and read in the same program
import time

from Utilities.WebCommunications import sendsensordata
from Controllers.DHT22 import readdhtsensor
import json
import RPi.GPIO as GPIO

def loop(minutes):
    while True:
        print("about to get a reading")
        print("turn on pin 27")
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(27, GPIO.OUT)
        print("Light On")
        GPIO.output(27, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(27, GPIO.LOW)

        # you may need to change this to number depending on where your sensor reading is going,ex GPIO17, would be 17
        pin = 18

        jsonreading = json.loads(readdhtsensor(pin))
        print(jsonreading['temperature'])
        sendsensordata(jsonreading['temperature'], jsonreading['humidity'], jsonreading['time'])

        # When we are complete with our testing, move the timeInterval to 10 - make sure that the sleep is 60 * minutes.
        time.sleep(1 * minutes)


# Set up a routine that runs every 15 minutes
# that's 15 minutes
timeInterval = 1
loop(timeInterval)