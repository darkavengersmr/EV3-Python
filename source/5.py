#!/usr/bin/env python3

from ev3dev.ev3 import *
from math import *
import time

btn = Button()

speed = 300

mA = LargeMotor('outA')
mD = LargeMotor('outD')

LS1 = LightSensor('in2')
LS2 = LightSensor('in3')
LS1.mode = 'REFLECT'
LS2.mode = 'REFLECT'

Gyro = GyroSensor("in1")
Gyro.mode = "GYRO-ANG"
                                                    
def motor(speed):    
    if speed>900:   
        speed = 900                             
    elif speed<-900:      
        speed = -900 
    return speed

mA.reset()
mD.reset()


e = 0
es = 0
u = 0
Pk = 3
Dk = 6

D = 0

while not btn.backspace:
    e = LS1.value()/10 - LS2.value()/10
    u = e*Pk + (e-es)*Dk    
    es = e
      
    mA.run_forever(speed_sp=motor(speed+u))
    mD.run_forever(speed_sp=motor(speed-u))

    if mA.position != mD.position:
        D = (61*(mA.position + mD.position))/(abs(mA.position-mD.position))
    print(D)


    if (mA.position*(56*pi/360)+mD.position*(56*pi/360))/2 > pi*(D*2) and time.time() > 3:
        break


mA.stop(stop_action="hold")
mD.stop(stop_action="hold")
Sound.beep()

grad = 0
ma = 0
mb = 0
time.sleep(1)
Gyro.mode = 'GYRO-RATE'
Gyro.mode = 'GYRO-ANG'

speedL = 0
speedR = 0

ma = mA.position
mb = mD.position

tmp = D
speed = 50

while not btn.backspace:
    ob = 56*pi/360
    if ((mA.position-ma)*ob+(mD.position-mb)*ob)/2 > (2*D)*tan(radians(0.5)):

        if mA.position > mD.position:
            grad = grad+1             
        else:
            grad = grad-1
        
        D = D-tmp/720
        ma = mA.position
        mb = mD.position
 

    speedL = speed-(Gyro.value()-grad)*10
    speedR = speed+(Gyro.value()-grad)*10

    mA.run_forever(speed_sp=motor(speedL))
    mD.run_forever(speed_sp=motor(speedR))

    print(D)
    if D<0.5:
        break


mA.stop(stop_action="hold")
mD.stop(stop_action="hold")
Sound.beep()
