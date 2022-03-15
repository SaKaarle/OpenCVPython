#https://www.alirookie.com/post/python-opencv-fullscreen-webcam-video-improve-image-quality
#https://techtutorialsx.com/2020/05/07/python-opencv-saving-video-from-webcam/
#https://cvexplained.wordpress.com/2020/04/28/color-detection-hsv/
# https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv

import cv2 
import numpy as np



capture = cv2.VideoCapture(0)

while (True):
 
    ret, frame = capture.read()
     

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([70,50,50])
    upper_blue = np.array([120,255,255])

    lower_green = np.array([40,40,40])
    upper_green = np.array([70,255,255])

# lower boundary RED color range values; Hue (0 - 10)
    lower1 = np.array([0, 100, 20])
    upper1 = np.array([10, 255, 255])
 
# upper boundary RED color range values; Hue (160 - 180)
    lower2 = np.array([160,100,20])
    upper2 = np.array([179,255,255])
 
    lower_mask = cv2.inRange(hsv, lower1, upper1)
    upper_mask = cv2.inRange(hsv, lower2, upper2)
 
    Rmask =  lower_mask + upper_mask;
    # Threshold the HSV image to get only blue colors
    Bmask = cv2.inRange(hsv, lower_blue, upper_blue)
    Gmask = cv2.inRange(hsv, lower_green,upper_green)
    #Rmask = cv2.inRange(hsv, lower2,upper2)
    # Bitwise-AND mask and original image
    Bres = cv2.bitwise_and(frame,frame, mask= Bmask)
    Gres = cv2.bitwise_and(frame,frame, mask= Gmask)
    Rres = cv2.bitwise_and(frame,frame, mask= Rmask)

    #cv2.imshow('video', frame)
    cv2.imshow('frame',frame)
    #cv2.imshow('Blue mask',Bmask)
    #cv2.imshow('Green mask', Gmask)
    #cv2.imshow('Red mask', Rmask)

    cv2.imshow('Blue res',Bres)
    cv2.imshow('Green res',Gres)
    cv2.imshow('Red res',Rres)
    
    if cv2.waitKey(1) != -1:
        break
 
capture.release()
cv2.destroyAllWindows()