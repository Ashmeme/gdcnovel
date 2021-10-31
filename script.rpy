# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Student",color="#c8c8ff")
define e = Character("Old Student",color="#00c8ff")

image main = im.Scale("main_lobby.png",1280,720)
image bgcanteen = im.Scale("stolov.jpg",1280,720)
image stairs = im.Scale("stairs.png",1280,720)
image obsh = im.Scale("obshaga1.png",1280,720)
image gym = im.Scale("gym.png",1280,720)
image os = im.Scale("os.png",1280,720)
default Location = "Obshaga1"

# The game starts here.

screen time:
    frame:
        xalign 0.05
        yalign 0.1
        vbox:
            if minutes<10:
                
                text '[hour]:0[minutes]'
            else:
                text '[hour]:[minutes]'
screen denjata:
    frame:
        xalign 0.05
        yalign 0.15
        vbox:
            text '$[money]'

label start:
    call variables from _call_variables
    show screen time with dissolve
    show screen denjata with dissolve
    
    scene obsh with fade
    
        
    s "New day, huh..."
    menu:
        "look up shop":
            call shop1 from _call_shop1
        
        "Go to uni":
            pass
    
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
            menu:
            
                "Go to OpenSpace":
                    $ Location = "os"
                    jump event1
                "Go to gym":
                    $ Location = "gym"
                    jump event2
                "Go to Cafeteria":
                    $ Location = "cafeteria"
                    jump event3
                
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
                scene gym with fade
                "Gotta work out"
                $ hour+=1
                $ minutes+=30
                jump loop
            
            label event3:
                scene bgcanteen with fade
                menu:
                    "Stand in line":
                        s "Man, this line takes forever..."
                        "..."
                        "..."
                        "..."
                        call screen canteen
                        
                        
                        s "Gotta sit somewhere..."
                        jump event4
                        
                    "Walk Around":
                        jump event4
            label event4:
                s "oh shit, I see some familiar faces!" 
                "..."
                "Time spent"
                $ minutes+=30
                jump loop
    return
        
 
    label variables:
        $ running = 1
        $ money=3000
        $ hour = 8
        $ minutes=0