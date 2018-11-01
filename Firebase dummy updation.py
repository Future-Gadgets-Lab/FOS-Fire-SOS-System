import pyrebase
import platform
import os
import glob
import time
import cv2
import time

config={        #fill according to your firebase database
    "apiKey": "AIzaSyDii0z_SxTaFpUwwTNkw3m8B7rIh5OEImM",
    "authDomain": "lifesaver-18f28.firebaseapp.com",
    "databaseURL": "https://lifesaver-18f28.firebaseio.com/",
    "storageBucket": "lifesaver-18f28.appspot.com"
}
firebase =pyrebase.initialize_app(config)
db=firebase.database()
#def stream_handler(message):
#    print(message["data"])

while(True):
    #my_stream = db.child("Cars").child(Plate).stream(stream_handler)
    db.child("user").child("Dummy").child("Dummy").child('lat').set(27.65)
    #print(time.time())
    db.child("user").child("Dummy").child("Dummy").child('long').set(77.11)
    db.child("user").child("Dummy").child("Dummy").child('severity').set(1)
    db.child("user").child("Dummy").child("Dummy").child('spread').set(30)
    db.child("user").child("Dummy").remove()
