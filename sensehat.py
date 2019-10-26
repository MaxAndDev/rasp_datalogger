from sense_hat import SenseHat
station_id=1
sense = SenseHat()
sense.clear()
pressure = sense.get_pressure()
temp = sense.get_temperature()
humidity = sense.get_humidity()

from datetime import datetime
now = datetime.now()
print(now)

output = {
    "station_id": station_id,
    "airpressure": pressure,
    "humidity": humidity,
    "temperature": temp,
    "timestamp": now,
    "latitude": 50.9271,
    "longitude": 11.5892,
    "position_tag": "kitchen"
  }
  
print(output)
import json
outputJson = json.dumps(output)

print(type(outputJson))

# for HTTP Post: https://www.geeksforgeeks.org/get-post-requests-using-python/
# for simu: https://trinket.io/sense-hat
