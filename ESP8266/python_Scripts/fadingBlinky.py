'''
Copyright: 
Mohammad Safeea, 9-Oct-2019
About:
fadingBlinky.py is a microPython script for
ESP8266. It is used to blink the built-in
led (with fading effect) using PWM signal.
'''
from machine import Pin
from machine import PWM
from time import sleep

# Initiate output pin
LedBuiltin=2
p=Pin(LedBuiltin,Pin.OUT)
pwm=PWM(p)

# Initiate some variables
i=1024
delta=256
flag=-1
max=i+delta
min=i-delta

# Control loop
while 1:
    i=i+2*flag
    if i>max:
        flag=-1
    if i<min:
        flag=1
    pwm.duty(i)
    sleep(0.01)