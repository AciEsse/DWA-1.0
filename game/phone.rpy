label home_message:

    show aci phone at right

    if amore and amicizia > 3:

        "Ciao, mi sono divertito molto oggi con te"
        #show aci normal
        menu:
            "Anch'io, non vedo l'ora che sia domani!":
                call love_increased from _call_love_increased
                #show aci giggle #foto finestra
                "Amore +1"
            "Bah, io non molto":
                call hate_increased from _call_hate_increased
                call hate_increased from _call_hate_increased_1
                call hate_increased from _call_hate_increased_2
                #show aci surprised #foto finestra
                aci "Ah si?"
                "Antipatia +3"

    else:
        #aggiungere foto a finiestra di dialogo
        "Ciao, ci vediamo domani per le 9:00?"
        menu:
            "Si, certo":
                #show aci smile #foto finestra
                call friendship_increased from _call_friendship_increased
                "Amicizia +1"

            "Mmh, credo che domani dormirò tutto il giorno":
                #show aci surprised #foto finestra
                #show aci surprised #foto finestra
                aci "Ma che stai dicendo? L'esame è alle porte!"
                call hate_increased from _call_hate_increased_3
                "Antipatia +1"

    #show aci normal #aggiungi finestra
    "A domani allora!"
    hide aci phone

    jump home_2
