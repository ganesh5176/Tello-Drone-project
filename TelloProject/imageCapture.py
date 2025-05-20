from djitellopy import tello
import cv2
import time

#After dowloding tello libary with commands
#Just named tello object ganesh, when the drone connects with program 
#It will print it's battery

ganesh = tello.Tello()
ganesh.connect()
print(ganesh.get_battery())




ganesh.streamon()

while True:
    img = ganesh.get_frame_read().frame
    img = cv2.resize(img, (360,240))
    cv2.imshow("Image", img)#this will create a window to show the capture
    cv2.waitKey(2)#if we dont write this 