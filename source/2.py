#!/usr/bin/env python3

from ev3dev.ev3 import *
from time import sleep

btn = Button()

tr = 1

color = [Leds.RED, Leds.GREEN, Leds.AMBER, Leds.ORANGE, Leds.YELLOW]
cs = 0

Leds.all_off()
 
on = 127

while not btn.backspace:
    if btn.check_buttons(buttons=['left']):
        cs=cs-1
        if cs<0:
            cs=4

        Sound.speak("Button left")
        Leds.set_color(Leds.LEFT, color[cs], on/255)
        Leds.set_color(Leds.RIGHT, color[cs], on/255)
        sleep(0.5)   

    elif btn.check_buttons(buttons=['right']):
        cs=cs+1
        if cs>4:
            cs=0

        Sound.speak("Button right")
        Leds.set_color(Leds.LEFT, color[cs], on/255)
        Leds.set_color(Leds.RIGHT, color[cs], on/255)
        sleep(0.5)

    if btn.check_buttons(buttons=['up']):
        on=on+10
        if on>240:
            Sound.speak("Maximum")
            on=255
        Leds.set_color(Leds.LEFT, color[cs], on/255)
        Leds.set_color(Leds.RIGHT, color[cs], on/255)
        sleep(0.1)
    elif btn.check_buttons(buttons=['down']):
        on=on-10
        if on<10:
            Sound.speak("Minimum")
            sleep(2)
            on=0
        
        Leds.set_color(Leds.LEFT, color[cs], on/255)
        Leds.set_color(Leds.RIGHT, color[cs], on/255)
        sleep(0.1)

    if btn.check_buttons(buttons=['enter']):
        Sound.speak("Random color")
        tr = 1
        while not btn.backspace or tr!=0:
            Leds.set_color(Leds.RIGHT, Leds.RED,0)
            Leds.set_color(Leds.LEFT, Leds.GREEN,0)
            
            
            for i in range(0,255,5):
                Leds.set_color(Leds.LEFT, Leds.GREEN,i/255)
                if btn.check_buttons(buttons=['backspace']):
                    tr = 0            
            if tr == 0:
                break                

            for i in range(255,0,-5):
                Leds.set_color(Leds.RIGHT, Leds.ORANGE,(255-i)/255) 
                Leds.set_color(Leds.LEFT, Leds.GREEN,i/255) 
                
                if btn.check_buttons(buttons=['backspace']) or tr == 0:
                    break              
        
            for i in range(0,255,5):
                Leds.set_color(Leds.LEFT, Leds.GREEN,i/255)
                if btn.check_buttons(buttons=['backspace']):
                    tr = 0
            if tr == 0:
                break
            Leds.set_color(Leds.RIGHT, Leds.ORANGE,1)

            for i in range(255,0,-5):
                Leds.set_color(Leds.RIGHT, Leds.ORANGE,i/255)
                Leds.set_color(Leds.LEFT, Leds.GREEN,i/255)

                if btn.check_buttons(buttons=['backspace']): 
                    break  
            for i in range(0,255,5):
                Leds.set_color(Leds.LEFT, Leds.YELLOW,i/255)
                if btn.check_buttons(buttons=['backspace']):
                    tr = 0
            if tr == 0:
                break

            for i in range(255,0,-5):
                Leds.set_color(Leds.RIGHT, Leds.RED,(255-i)/255)
                Leds.set_color(Leds.LEFT, Leds.YELLOW,i/255)

                if btn.check_buttons(buttons=['backspace']) or tr == 0:
                    break

            for i in range(0,255,5):
                Leds.set_color(Leds.LEFT, Leds.YELLOW,i/255)
                if btn.check_buttons(buttons=['backspace']):
                    tr = 0
            if tr == 0:
                break
            Leds.set_color(Leds.RIGHT, Leds.RED,1)

            for i in range(255,0,-5):
                Leds.set_color(Leds.RIGHT, Leds.RED,i/255)
                Leds.set_color(Leds.LEFT, Leds.YELLOW,i/255)

                if btn.check_buttons(buttons=['backspace']):
                    break
