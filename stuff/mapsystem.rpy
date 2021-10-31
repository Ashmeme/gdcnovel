screen canteen:
    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        ysize 300
        vbox:
            text "menu:"
            textbutton "BUY SPAGHET\n700" action SetVariable("money",money-700)

            textbutton "BUY SOUP\n500" action SetVariable("money",money-500)

            textbutton "BUY RICE'A'RONI\n800" action SetVariable("money",money-800)
                
            textbutton "close" action Return()

label shop1:
        show e usual
        e "Need Something?"
        call screen shop
screen shop:
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 700
        vbox:
            text "menu:"
            
            textbutton "govno 1\n300" action SetVariable("money",money-300)
            textbutton "govno 2\n200" action SetVariable("money",money-200)
            textbutton "govno 3\n100" action SetVariable("money",money-100)
            
            textbutton "close" action Return()