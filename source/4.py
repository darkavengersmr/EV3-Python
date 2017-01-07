#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
from math import *

ma = 0
md = 0

btn = Button()
speed = 200

mA = LargeMotor('outA')
mD = LargeMotor('outD')

IR = InfraredSensor('in4')
Gyro = GyroSensor("in1")

Gyro.mode = 'GYRO-ANG'

def motor(speed):
    if speed>900:
        speed = 900
    elif speed<-900:
        speed = -900
    return speed



MIN = 100
MINGRAD = 0

g = [0 for i in range(360)]

mA.run_forever(speed_sp=speed)
mD.run_forever(speed_sp=-1*speed)

while Gyro.value() < 359:
    GyVal =  Gyro.value()

    g[GyVal] = IR.value()*0.7
    if g[GyVal] < MIN:
        MIN = g[GyVal]
        MINGRAD = GyVal    

mA.stop(stop_action="hold")
mD.stop(stop_action="hold")

Sound.beep()

MINGRAD = MINGRAD + 90

while abs(Gyro.value()-MINGRAD) > 1:
    speedL = -1*(Gyro.value()-MINGRAD)*5
    speedR = (Gyro.value()-MINGRAD)*5
    mA.run_forever(speed_sp=motor(speedL))
    mD.run_forever(speed_sp=motor(speedR))

mA.stop(stop_action="hold")
mD.stop(stop_action="hold")

sleep(2)

Gyro.mode = 'GYRO-RATE'
Gyro.mode = 'GYRO-ANG'

sleep(1)

grad = 0
i = 2*(MIN*6+70)*tan(radians(0.5))

mA.reset()
mD.reset()

speed = 50

while grad > -360 and not btn.backspace:
    ob = 56*pi/360
    if ((mA.position-ma)*ob+(mD.position-md)*ob)/2 > i:
        grad = grad-1
        ma = mA.position
        md = mD.position

    speedL = speed-(Gyro.value()-grad)*16
    speedR = speed+(Gyro.value()-grad)*16

    mA.run_forever(speed_sp=motor(speedL))
    mD.run_forever(speed_sp=motor(speedR))
 

mA.stop(stop_action="hold")
mD.stop(stop_action="hold") 
