# Time and read in the same program
import time

from Utilities.WebCommunications import sendsensordata
from Controllers.DHT22 import readdhtsensor
import json


def loop(minutes):
    while True:
        print("about to get a reading")

        # you may need to change this to number depending on where your sensor reading is going,ex GPIO17, would be 17
        pin = 4

        jsonreading = json.loads(readdhtsensor(pin))
        print(jsonreading['temperature'])
        sendsensordata(jsonreading['temperature'], jsonreading['humidity'], 1)

        # When we are complete with our testing, move the timeInterval to 10 - make sure that the sleep is 60 * minutes.
        time.sleep(60 * minutes)


# Set up a routine that runs every 15 minutes
# that's 15 minutes
timeInterval = 10
loop(timeInterval)