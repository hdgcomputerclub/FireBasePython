import Adafruit_DHT
import datetime
import json


def readdhtsensor(pinNumber):
    sensor = Adafruit_DHT.DHT22
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pinNumber)
    # date_string = f'{datetime.datetime.now():%Y-%m-%d %H:%M:%S%z}'
    return json.dumps({"humidity": humidity, "temperature": temperature, "time": str(datetime.datetime.now())})
