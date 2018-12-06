

# Time and read in the same program
import time

# import getnode library to return mac address as 48 bit integer
from uuid import getnode as get_mac
mac= get_mac()              #mac address variable as 48 bit integer
print(mac)

from Utilities.WebCommunications import sendsensordata
from Controllers.DHT22 import readdhtsensor
import json
import RPi.GPIO as GPIO

# change this variable to location of device
roomid="Computer Lab"

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
        print(jsonreading)
        sendsensordata(jsonreading['temperature'], jsonreading['humidity'], roomid)

        # When we are complete with our testing, move the timeInterval to 10 - make sure that the sleep is 60 * minutes.
        time.sleep(5 * 60 * minutes)


# Set up a routine that runs every 15 minutes
# that's 15 minutes
timeInterval = 1
loop(timeInterval)