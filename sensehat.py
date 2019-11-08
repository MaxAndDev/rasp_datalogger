from sense_hat import SenseHat
station_id=1
sense = SenseHat()
sense.clear()
pressure = sense.get_pressure()
temp = sense.get_temperature()
humidity = sense.get_humidity()

sense.show_message("Seminar Data Logger")

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
import json

# for HTTP Post: https://www.geeksforgeeks.org/get-post-requests-using-python/
# test api --- https://www.geeksforgeeks.org/get-post-requests-using-python/
import requests

API_ENDPOINT = "http://10.231.200.105:3000/data"
API_KEY = ""

#r = requests.post(url = API_ENDPOINT, data = output)


## rsa Kryptografie --------- https://stackoverflow.com/questions/30056762/rsa-encryption-and-decryption-in-python

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate pub and priv key

publickey = key.publickey() # pub key export for exchange
# privatekey = key.decrypt
encrypted = publickey.encrypt('encrypt this message', 32)

print( 'encrypted message:', encrypted) #ciphertext
f = open('encryption.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open('encryption.txt', 'r')
message = f.read()


decrypted = key.decrypt(ast.literal_eval(str(encrypted)))

print('decrypted', decrypted)

f = open ('encryption.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()
