import serial
import requests
from urllib.request import urlopen
import json

ser = serial.Serial("COM4", 9600)
url = "http://127.0.0.1:8000/home/api"

while True:
    bin_data = ser.readline()
    bad_data = bin_data.decode()
    # print(bad_data)
    # data = bad_data.strip()

    # Cleaning data
    # """
    datastring = '{"name": "Tulip","next_spray": "01:02:03","fertilizer_level": 50,"led_intensity": 90,"time_to_sundown": "19:00:00","status": "H",'
    a = bad_data.split(',')
    for i in a[:-1]:
        l = i.split("=")
        try:
            datastring += f'"{l[0]}": {float(l[1])},'
        except ValueError:
            string = l[1].strip();
            if string == "NAN":
                datastring += f'"{l[0]}": 0.0,'
            else:
                datastring += f'"{l[0]}": "{string}",'
        
    l = a[-1].split("=")
    try: 
        datastring +=  f'"{l[0]}": {float(l[1])}' + '}'
    except ValueError:
        string = l[1].strip()
        if string == "NAN":
            datastring +=  f'"{l[0]}": 0.0' + '}'
        datastring +=  f'"{l[0]}": "{string}"' + '}'

    print(datastring)
    # """

    # response = urlopen(url)
    # data_json = json.loads(response.read())

    # datastring = '{"name": "Tulip","temp": 0,"humidity": 40,"next_spray": "01:02:03","fertilizer_level": 50,"led_intensity": 90,"time_to_sundown": "19:00:00","status": "H"}'
    # print(data)
    json_object = json.dumps(datastring, indent=4)
    print(json_object)
    r = requests.put('http://127.0.0.1:8000/home/api/1/', data=datastring)

    print(r)

"""
"{\"name\": \"Tulip\",\"temp\": 0,\"humidity\": 40,\"next_spray\": \"01:02:03\",\"fertilizer_level\": 50,\"led_intensity\": 90,\"time_to_sundown\": \"19:00:00\",\"status\": \"H\"}"


"{\"name\": \"Tulip\",\"next_spray\": \"01:02:03\",\"fertilizer_level\": 50,\"led_intensity\": 90,\"time_to_sundown\": \"19:00:00\",\"status\": \"H\"}\"temp\": 0,\"humidity\": 0,\"led_intensity\": 0}"
"""