# Copyright: Mohammad Safeea. 27-Sept-2019

# Following secript performs a get request whenever a change in the state of Pin 5 occurs
import urequests
from machine import Pin
import time
# Configure D1 as an input
p=Pin(5,Pin.IN,Pin.PULL_UP) 
# NodeMCU micropython pinout for (D1) is (GPIO5)

# Following is to establish a wifi connection
import network
station=network.WLAN(network.STA_IF)
station.active(True)
station.connect("NAME OF NETWOR","PASSWORD")
print(station.isconnected())
# Following is a loop for the control-logic
while 1:
    # check the state of Pin D1 (GPIO5)
    val_1=p.value()
    time.sleep(0.002) # sleep for 2 milliseconds
    val_2=p.value()
    if (val_1==0)and(val_2==1):
        print("Rising edge is deteceted, sending a get request")
        # Following for Https request,
        # Request is to IFTTT website
        r=urequests.get('https://maker.ifttt.com/trigger/{EVENT NAME}/with/key/{YOUR KEY}')
        print(r)
        time.sleep(1) # sleep for one second
    if (val_1==1)and(val_2==0):
        print("Falling edge is deteceted, sending a get request")
        r=urequests.get('https://maker.ifttt.com/trigger/{EVENT NAME}/with/key/{YOUR KEY}')
        print(r)
        time.sleep(1) # sleep for one second