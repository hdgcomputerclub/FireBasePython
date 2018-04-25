#Time and read in the same program

import time

import Adafruit_DHT

def loop(minutes):
    while True:

        sensor = Adafruit_DHT.AM2302
        pin = '4'           #you may need to change this to number depending on where your sensor reading is going,ex GPIO17, would be 17
        # Try to grab a sensor reading.  Use the read_retry method which will retry up
        # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        # Un-comment the line below to convert the temperature to Fahrenheit.
        temperature = temperature * 9 / 5.0 + 32

        # Note that sometimes you won't get a reading and
        # the results will be null (because Linux can't
        # guarantee the timing of calls to read the sensor).
        # If this happens try again!
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')


        time.sleep(60 * minutes)


# Set up a routine that runs every 15 minutes
timeInterval =  15 # thats 15 minutes
loop(timeInterval)