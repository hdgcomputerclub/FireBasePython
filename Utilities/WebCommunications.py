
import requests
API_ENDPOINT = "https://webhook.site/63862a39-6e44-4043-a56a-f4c1c095345b"


def sendsensordata(temp, humidity, datetime):
    json_data = {
        "humidity":humidity,
        "temperature":temp,
        "datetime": datetime
    }
    r = requests.post(url=API_ENDPOINT, data= json_data)
    print(r)


