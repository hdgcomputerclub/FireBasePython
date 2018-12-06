
import requests
import json

# API_ENDPOINT = "http://localhost:3000/api/saveTemperaturePost"
API_ENDPOINT = "http://www.climaedu.com/api/saveTemperaturePost"


def sendsensordata(temperature, humidity, roomId):
    headers = {'content-type': 'application/json', 'Accept': 'text/plain'}
    json_data = {
        "humidity": humidity,
        "temperature": temperature,
        "roomId": roomId
    }
    dataoutput = json.dumps(json_data)
    print(dataoutput)
    r = requests.post(url=API_ENDPOINT, data=dataoutput, headers=headers).json()
    print(r["results"])


