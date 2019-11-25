from sense_hat import SenseHat
import requests
import time
sense = SenseHat()
sense.clear()
from time import sleep


def getparam():
  station_id=1
  pressure = sense.get_pressure()
  temp = sense.get_temperature()
  humidity = sense.get_humidity()
  from datetime import datetime
  now = datetime.now()
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
  return output

def makepost(inputdata):
  try:
    API_ENDPOINT = "http://10.231.192.210:3000/data"
    r = requests.post(url = API_ENDPOINT, data = inputdata,timeout=1)
    #response = r.text
    response = r.status_code
    print(response)
    sleep(0.5)
    sense.set_pixel(0, 0, (0, 0, 255))
    sleep(0.5)
    sense.set_pixel(0, 0, (0, 0, 0))
  except:
    print("nicht funktioniert")
    sleep(0.5)
    sense.set_pixel(1, 0, (255, 0, 0))
    sleep(0.5)
    sense.set_pixel(1, 0, (0, 0, 0))
  

  #print(inputdata)


def showmenu():
  # farben: 
  g = (0, 255, 0) # Green
  b = (0, 0, 0) # Black
  c = (50,50,50)
  creeper_pixels = [
    b, b, b, b, b, b, b, b,
    b, b, b, g, b, g, b, b,
    b, b, b, b, g, b, b, b,
    b, b, b, b, b, b, b, b,
    b, b, b, g, b, g, b, b,
    b, b, b, b, g, b, b, b,
    b, b, b, g, b, g, b, b,
    b, b, b, b, b, b, b, b
  ]
  sense.set_pixels(creeper_pixels)

def showexit():
  g = (0, 255, 0) # Green
  b = (0, 0, 0) # Black
  c = (50,50,50)
  creeper_pixels = [
    b, b, b, b, b, b, b, b,
    b, g, b, b, b, b, g, b,
    b, b, g, b, b, g, b, b,
    b, b, b, g, g, b, b, b,
    b, b, b, g, g, b, b, b,
    b, b, g, b, b, g, b, b,
    b, g, b, b, b, b, g, b,
    b, b, b, b, b, b, b, b
  ]
  sense.set_pixels(creeper_pixels)

showmenu()
events = True
while events:
  for event1 in sense.stick.get_events():
    if event1.action == "pressed":
      if event1.direction == "up":
        sense.set_pixel(7, 1, (255, 255, 0))
        sense.set_pixel(7, 5, (0, 0, 0))
      #print("a")
      #events = False
        measure = True
        while measure:
          makepost(getparam())
          for event2 in sense.stick.get_events():
            if event2.action == "pressed":
              if event2.direction == "down":
                sense.set_pixel(7, 5, (255, 255, 0))
                sense.set_pixel(7, 1, (0, 0, 0))
                measure = False  
      if event1.direction == "down":
        showexit()
        sleep(2)
        sense.clear(0,0,0)
        events = False
      if event1.direction == "right":
        sense.clear(0,0,0)


#sense.show_message("Seminar Data Logger")


# for HTTP Post: https://www.geeksforgeeks.org/get-post-requests-using-python/
# test api --- https://www.geeksforgeeks.org/get-post-requests-using-python/








## rsa Kryptografie --------- https://stackoverflow.com/questions/30056762/rsa-encryption-and-decryption-in-python

""" 
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
"""
