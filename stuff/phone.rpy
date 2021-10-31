screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/phone_%s.png"
        action ShowMenu("phoneUI")
        
screen phoneUI:
    add "UI/bg phone.png"
    
    frame:
        xalign 0.4
        yalign 0.5
        text "UNDER CONSTRUCTION :("
        #xpadding 10
        #ypadding 10
        
        #vbox:
        
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/return_%s.png"
        action Return()
