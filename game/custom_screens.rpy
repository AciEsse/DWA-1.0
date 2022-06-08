# Bottone Statistiche e Oggetti
    screen gameUI:
        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -50
            yoffset 15
            idle "pulcino_stats_idle.png"
            hover "pulcino_stats_hover.png"
            action ShowMenu ("StatsUI")

    screen StatsUI:
        frame:
            #add "bg pink.png"
            xalign 0.5
            yalign 0.5
            xpadding 30
            ypadding 30

            hbox:
                spacing 40

                vbox:
                    spacing 10
                    text "STATISTICHE:" size 18
                    text "{image=handshake.png}{alt}Amicizia{/alt}  Amicizia: [amicizia]" size 20 color "#99ff99"
                    text "{image=heart.png}{alt}Amore{/alt}  Amore: [amore]" size 20 color "#ffccff"
                    text "{image=ungry.png}{alt}ungry{/alt}  Antipatia: [antipatia]" size 20 color "#66ccff"
                    #text "__________________" size 15
                    text "RISORSE:" size 18
                    text "{image=money.png}{alt}money{/alt}  Soldi: € [soldi]" size 20 color "#ffff99"
                    text "{image=essePoints.png}{alt}esse{/alt}  Punti Esse: [puntiEsse]" size 20 color "#cc66ff"


        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -50
            yoffset 15
            idle "pulcino_stats_idle.png"
            hover "pulcino_stats_hover.png"
            action Return()
