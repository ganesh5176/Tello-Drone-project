from djitellopy import tello
from time import sleep

#After dowloding tello libary with commands
#Just named tello object ganesh, when the drone connects with program 
#It will print it's battery

ganesh = tello.Tello()
ganesh.connect()
print(ganesh.get_battery())

#this section is on how to control the drone
ganesh.takeoff()
#This will control the diracton the drone will move 
ganesh.send_rc_control(0, 50, 0, 0)
sleep(2)
ganesh.send_rc_control(30, 0, 0, 0)
sleep(2)
ganesh.send_rc_control(0, 0, 0, 0)
ganesh.land()