#!/usr/bin/env python3

from ev3dev.ev3 import *

mB = LargeMotor('outA')
mC = LargeMotor('outD')
Sound.beep().wait()
mB.stop(stop_action="hold")
mC.stop(stop_action="hold")
Sound.beep().wait()
