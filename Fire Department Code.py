import pyrebase
import platform
import os
import glob
import time
import cv2
import winsound
import time
from gmplot import gmplot
config={        #fill according to your firebase database
    "apiKey": "AIzaSyDii0z_SxTaFpUwwTNkw3m8B7rIh5OEImM",
    "authDomain": "lifesaver-18f28.firebaseapp.com",
    "databaseURL": "https://lifesaver-18f28.firebaseio.com/",
    "storageBucket": "lifesaver-18f28.appspot.com"
}
firebase =pyrebase.initialize_app(config)
db=firebase.database()
count=0
lat=0
long=0
def stream_handler(message):
    #print(time.time())
    lat=[]
    long=[]
    print(message["data"])
    for key in message["data"].items():
        for k in key[1].items():
            #print("lat", k[1]["lat"])
            #print("long", k[1]["long"])
            lat.append(k[1]["lat"])
            long.append(k[1]["long"])
    if(lat!=[] and long!=[]):
        gmap = gmplot.GoogleMapPlotter(lat[1], long[1], 13)
        for i in range(len(lat)):
            # Scatter points
            top_attraction_lats, top_attraction_lons = zip(*[(lat[i], long[i])])
            gmap.scatter(top_attraction_lats, top_attraction_lons, '#3B0B39', size=40, marker=False)

            # Marker
            hidden_gem_lat, hidden_gem_lon = lat[i], long[i]
            gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')
        # Draw
        gmap.draw("my_map.html")
    winsound.PlaySound('sound5.wav',winsound.SND_FILENAME)
print("Listening to stream")
my_stream = db.child("user").stream(stream_handler)
hi=0
while(True):
    hi=1
