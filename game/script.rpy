﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Student",color="#c8c8ff")

image main = im.Scale("main_lobby.png",1280,720)
image stairs = im.Scale("stairs.png",1280,720)
image obsh = im.Scale("obshaga1.png",1280,720)
image gym = im.Scale("gym.png",1280,720)
image os = im.Scale("os.png",1280,720)
default Location = "Obshaga1"

# The game starts here.

label start:
    call variables from _call_variables
    scene obsh
    with fade
        
    s "Damn, this lecture is too early today"
    s "Gotta go to campus..."
    "Current Time is [hour]:0[minutes]"
    
    
    show screen gameUI
    s "Future dialogue"
    $ minutes+=15
    label loop:
    
        while running:
            scene main
            with fade
            
            if minutes>60:
                $ hour+=1
                $ minutes=0
            if hour > 20:
                s "It's already late..."
                s "I should go back home"
                return
            
            if minutes<10:
                
                "Current Time is [hour]:0[minutes]"
            else:
                "Current Time is [hour]:[minutes]"
            
            menu:
            
                "Go to OpenSpace":
                    $ Location = "os"
                    jump event1
                "Go to gym":
                    $ Location = "gym"
                    jump event2
                
            label event1:
                scene os
                with fade
                s "I'm in [Location]!"
                "A new challenge comes up!"
                "*Event trigger*"
                $ hour+=3
                $ minutes+=20
                jump loop
            
            label event2:
                scene gym
                "Gotta work out"
                $ hour+=1
                $ minutes+=30
                jump loop
    return
 
    label variables:
        $ running = 1
        $ Money=30000
        $ hour = 8
        $ minutes=0