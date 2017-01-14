#! python3
# quickWeather.py - Prints the weather for a location from the command line.

import json, requests, sys

# Compute location from command line arguments.

if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from api

# City ID, Boston: 4317656
url = 'http://api.openweathermap.org/data/2.5/forecast/city?id=%s&APPID=ef8d04e9627de9c62c1f8868c84cb595' % (location)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a python variable

weatherData = json.loads(response.text)

# Print weather descriptions

w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
