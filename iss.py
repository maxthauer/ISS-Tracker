#!/usr/local/bin/python3
'''
Show who is currently in space using the opennotify api and Google Maps
It's important to know where astronauts are
Specify a path in the path variable below where your html file will be saved.


'''
import requests, json
import time  
from datetime import datetime

i = 0

path = "/Users/maximillianthauer/Desktop/iss.html"

peopleUrl = requests.get("http://api.open-notify.org/astros.json")
locationUrl = requests.get("http://api.open-notify.org/iss-now.json")
peopleData = peopleUrl.json()
locationData = locationUrl.json()
validAtTime = locationData['timestamp']
issLat = locationData['iss_position']['latitude']
issLong = locationData['iss_position']['longitude']
issLat = str(issLat)
issLong = str(issLong)
validAtTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(validAtTime))

htmlContent = """
<!DOCTYPE html>
<html>
   <head>
   <meta http-equiv="refresh" content="5">
   <h2>Current location of the ISS:</h2>
      <script src = "http://maps.googleapis.com/maps/api/js"></script>
      <script>
         function loadMap() {		
            var mapOptions = {
               center:new google.maps.LatLng("""+issLat+""", """+issLong+"""),
               zoom:3
            }
            var map = new google.maps.Map(document.getElementById("sample"),mapOptions);
            var marker = new google.maps.Marker({
               position: new google.maps.LatLng("""+issLat+""", """+issLong+"""),
               map: map,
            });
         }
      </script>
   </head>
   <body onload = "loadMap()">
      <div id = "sample" style = "width:580px; height:400px;"></div>
   </body>
</html>
"""

f = open(path, "w")
f.write(htmlContent)
f.close

number = peopleData['number']
person = peopleData['people']
numberInt = int(number)
numberStr = str(number)

print ("\n")
print ("Data valid as of: {}\n".format(validAtTime))
print ("ISS Coordinates:")
print ("Latitude: {}   Longitude: {}\n".format(issLat,issLong))

print (numberStr,"people are currently aboard the ISS\n")

for person in person:
	name = peopleData['people'][i]['name']
	craft = peopleData['people'][i]['craft']
	i = i+1
	print ("{} is on the {}".format(name,craft))

	if i == number + number:
		exit()
