#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import *
from math import pi

btn = Button()

mA = LargeMotor('outA')
mD = LargeMotor('outD')

mA.reset()
mD.reset()

CS1 = LightSensor('in2')
CS2 = LightSensor('in3')

CS1.mode='REFLECT'
CS2.mode='REFLECT'

speed = 800
r = 0

u = 0
e = 0
es = 0
Pk = 1.1
Dk = 2

def motor(speed):
    if speed>900:
        speed = 900
    elif speed<-900:
        speed = -900
    return speed

while not btn.backspace:
    e = CS1.value() - CS2.value()
    u = e*Pk + (e-es)*Dk
    es = e

    mA.run_forever(speed_sp=motor(speed+u))
    mD.run_forever(speed_sp=motor(speed-u))

    if mD.position != mA.position:
        r = (61*(mA.position + mD.position))/(abs(mD.position-mA.position))
    print(r)   


    sleep(0.01)
    if (mA.position*(pi*56/360)+mD.position*(pi*56/360))/2 > pi*(r*2) and time()>3:
        break


mA.stop(stop_action="hold")
mD.stop(stop_action="hold")

Sound.speak('Stoped').wait()
Sound.speak(round(r*2)).wait()

