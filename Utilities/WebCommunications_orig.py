
import requests
API_ENDPOINT = "http://www.climaedu.com/api/saveTemperature"


def sendsensordata(temp, humidity, roomid):
    json_data = {
        "humidity":humidity,
        "temperature":temp,
        "roomid" : roomid,
    }
    print(json_data)
    NEWAPI_ENDPOINT = API_ENDPOINT + "/" + str(temp) + "/" + str(humidity) + "/1"
    print(NEWAPI_ENDPOINT)
    r = requests.get(url=NEWAPI_ENDPOINT, data= json_data)
    print(r)




#def sendsensordata(temp, humidity, datetime, roomid, macaddress):
#    json_data = {
#        "humidity":humidity,
#        "temperature":temp,
#        "datetime": datetime,
#        "roomid" : roomid,
#        "macaddress" : macaddress
#    }
#    r = requests.post(url=API_ENDPOINT, data= json_data)
#    print(r)