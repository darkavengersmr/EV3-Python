#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep
import math

speed = 50
GyVal = 0

Gyro = GyroSensor("in1")
IR = InfraredSensor("in4")

mA = LargeMotor('outA')
mD = LargeMotor('outD')

Gyro.mode = "GYRO-ANG"



lcd = Screen()
lcd.draw.ellipse(( 84, 59,  94, 69))
lcd.draw.ellipse(( 25, 0,  153, 128))
lcd.update()

g = [0 for i in range(360)]

mA.run_forever(speed_sp=speed)
mD.run_forever(speed_sp=-1*speed)

while Gyro.value() < 360:
    GyVal =  abs(Gyro.value())    
    g[GyVal] = IR.value()*0.7

mA.stop(stop_action="hold")
mD.stop(stop_action="hold")  

for i in range(90):
    lcd.draw.line(( 89, 64,  89+g[i]*math.sin(math.radians(i)), 64-g[i]*math.cos(math.radians(i))))
    lcd.draw.line(( 89, 64,  89+g[i+90]*math.cos(math.radians(i)), 64+g[i+90]*math.sin(math.radians(i))))
    lcd.draw.line(( 89, 64,  89-g[i+180]*math.sin(math.radians(i)), 64+g[i+180]*math.cos(math.radians(i))))
    lcd.draw.line(( 89, 64,  89-g[i+270]*math.cos(math.radians(i)), 64-g[i+270]*math.sin(math.radians(i))))

lcd.update()
Sound.beep()

sleep(10)

