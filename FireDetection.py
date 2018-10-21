import cv2
import numpy as np

video = cv2.VideoCapture(0) #VideoCapture(0): opens the default camera
 
while True:
    (boolval, frame) = video.read() #reads the input frames
    if not boolval:
        break   

    #Read(): Grabs, decodes and returns the next video frame. 
    #If no frames has been grabbed (camera has been disconnected, 
    #or there are no more frames in video file), 
    #the methods (ret) return false and the functions return NULL pointer.


    blur = cv2.GaussianBlur(frame, (21, 21), 0) #Blurs an image using a Gaussian filter. 
    #The function convolves the source image with the specified Gaussian kernel(kernal size here is 21,21).
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
 
    lower = [19, 127, 240]
    upper = [88, 207, 253]
    
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    mask = cv2.inRange(hsv, lower, upper)
 
    output = cv2.bitwise_and(frame, hsv, mask=mask)
     #Calculates the per-element bit-wise conjunction of two arrays or an array and a scalar
    fire_thres= cv2.countNonZero(mask) #Counts non-zero array elements
    cv2.imshow("output", output)
    if int(fire_thres) > 4000: #compares the firevalue with the threshold
        print ('Fire detected')
    if cv2.waitKey(1)==27: #exists when escape is pressed.
        break
 
cv2.destroyAllWindows()
video.release()