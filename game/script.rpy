define aci = Character("Aci")
define prof = Character("Prof", color="#CD0000")
define Negoziante = Character("Negoziante", color="#66ff99")


label start:


    "Benvenuto a Date with Aci, una visual novel dove simulerai un appuntamento
     con Aci."
    show screen gameUI

    "Con i pulsanti in alto a destra potrai tenere traccia delle tue statistiche e delle tue risorse"
    "Nel gioco possiedi solo 3 punti esse, giocateli bene!"

#musica in background
label bgm:
    play music "audio/Solanin.ogg" fadein 1.0 volume 0.5
    $ message = False

#Creazione stats giocatore
default amicizia = 1
default amore = 1
default antipatia = 0

#Creazione oggetti del gioco
default soldi = 15
default cellulare = False
default cellulare2 = False
$ breaker = True # controlla se hai punti Esse sufficienti
default puntiEsse = 3
default offerta = 0 #Controlla se offri qualcosa
default richiesta = 0 # Contatore per offrire ad aci, lui accetterà solo alla terza volta


label inizio:
    "Buongiorno!"
    show aci smile



label background:
    scene bg uni
    show aci normal
    aci "Anche oggi in ritardo?"

label choices:
    aci "Hai studiato per l'esame di Videogames?"
    menu:
        "Si":
            jump choices1_a

        "mmh...":
            jump choices1_b

    label choices1_a:
        show aci giggle
        aci "Ottimo! Allora prendiamo questo 30!"
        jump choices1_common

    label choices1_b:
        show aci surprised
        aci "Come sarebbe a dire no?"
        jump choices1_common

    label choices1_common:
        show aci normal
        aci "Dai, andiamo in aula studio!"

label aulaStudio:
    scene bg lecturehall
    #with fade
    show aci normal
    aci "Per fortuna l'aula 4 oggi è vuota, dai mettiamoci a studiare.."
    show aci perplexed
    aci "..e questa volta senza 'pausa sigaretta'!"

label timeSkip:
    hide aci perplexed
    with fade
    "2 ore dopo.."
    show aci normal

label pausa:
    aci "Dai, abbiamo studiato due ore belle piene, ci siamo proprio meritati una pausa."
    aci "Andiamo a prendere un caffè al bar prima che inizi la lezione del professor Pippo?"
    menu:
        "Okay, prendiamoci un caffè!":
            show aci smile
            call friendship_increased from _call_friendship_increased_1
            call money_decreased from _call_money_decreased
            aci "Dai, andiamo"
            "Amicizia +1"
            "Costo del caffè: €1"
            "Soldi rimasti: €[soldi]"

        "Okay, oggi offro io!":
            show aci giggle
            call love_increased from _call_love_increased_1
            call money_decreased from _call_money_decreased_1
            call money_decreased from _call_money_decreased_2
            aci "Come farei senza di te?"
            "Amore +1"
            "Costo di due caffè: €2"
            "Soldi rimasti: €[soldi]"
            $ offerta += 1

        "Non mi piace molto il caffè..":
            show aci surprised
            call hate_increased from _call_hate_increased_4
            aci "Beh, puoi prendere anche un the o una bottiglietta d'acqua se preferisci."
            "Antipatia +1"


label relax:
    scene bg dib2
    with fade
    show aci giggle
    aci "E' davvero una bella giornata!"
    show aci normal
    aci "Dai che ne dici di quittare l'uni ed andare al parco a rilassarci? Tanto la lezione di Pippo inizia alle 15:30"
    menu:
        "Si, dai!":
            call friendship_increased from _call_friendship_increased_2
            show aci smile
            aci "Evvivaa!"
            "Amicizia +1"
            jump choicesPark

        "E se andassimo a casa tua?":
            #$ amore += 1
            show aci surprised
            aci "Casa mia? Ma è un peccato rimanere chiusi in casa quando le giornate sono così belle!"
            show aci normal
            aci "Dai, andiamo al parco!"
            jump choicesPark

        "Ma non avevi detto di voler studiare oggi?":
            call hate_increased from _call_hate_increased_5
            show aci surprised
            aci "Che noia! Si tratta solo di una pausa!"
            show aci sad
            aci "Come preferisci.."
            "Antipatia +1"
            jump choicesNoPark

label choicesPark:
    scene bg park
    show aci smile
    aci "Finalmente siamo arrivati!"
    aci "Dai, prendiamoci una Dregher al chioschetto!"

    label negozio:
        scene bg chiosco
        Negoziante "Salve le Dregher costano €1"
        Negoziante "Quante ne vuoi acquistare?"
        menu:
            "Compra 1 Birra":
                call money_decreased from _call_money_decreased_3
                "Costo della birra: €1"
                "Soldi rimasti: €[soldi]"
                show aci normal
                aci "Ci sta una birra rinfescante!"
            "Compra 2 Birre -- (1 punto Esse)":
                call checkEssePoints from _call_checkEssePoints
                #if puntiEsse < 1:
                if breaker == False:
                    jump negozio
                else:
                    call money_decreased from _call_money_decreased_4
                    call money_decreased from _call_money_decreased_5
                    #call essePoints_decreased
                    "Costo di due birre: €2"
                    "Soldi rimasti: €[soldi]"
                    #"Punti Esse rimasti: [puntiEsse]"
                    show aci surprised
                    aci "Mi vuoi davvero offrire una birra?"
                    show aci smile
                    aci "Grazie milleee"
                    if offerta > 0: ####### Se hai già offerto al bar guadagni più punti amore
                        show aci giggle
                        aci "Oggi mi stai viziando"
                        call love_increased from _call_love_increased_2
                        call love_increased from _call_love_increased_3
                        "Amore +2"
                    else:
                        call love_increased from _call_love_increased_4
                        "Amore +1"

            "Non acquistare nulla":
                show aci surprised
                aci "Credevo che volessi bere con me"
                call hate_increased from _call_hate_increased_6
                show aci sad
                "Antipatia +1"
                jump choicesNoPark


label choicesNoPark:
    scene bg dib2
    with fade
    "* 2 ORE DOPO *"
    show aci smile
    aci "Ormai è l'ora di pranzo."
    aci "Andiamo a mensa, ho rimediato due tessere da dei ragazzi del primo anno eheh"

label mensa:
    scene bg mensa
    show aci perplexed
    aci "Mi raccomando, se ti chiedono come ti chiami tu devi rispondere 'Andrea', sennò ci scopriranno e ci faranno pagare il pasto"
    menu:
        "O-okay!":
            show aci smile
            aci "Mi raccomando!"
            show aci normal
            aci "Si mangiaaa"

        "Non ce la faccio, mi viene l'ansia":
            show aci normal
            call hate_increased from _call_hate_increased_7
            aci "Non avere paura, io lo faccio sempre!"
            show aci perplexed
            aci "Voglio ricordarti che un pasto costa €5."
            "Antipatia +1"
            menu:
                "Okay, mi fido!":
                    show aci smile
                    aci "Ora si ragiona"
                    jump lezione


                "E se ci sgamano?":
                    show aci angry
                    call hate_increased from _call_hate_increased_8
                    aci "Come preferisci."
                    aci "Io sfrutterò la mia preziosissima tessera."
                    call mediumMoney_decreased from _call_mediumMoney_decreased
                    "Antipatia +1"
                    "Costo del pasto: €5"
                    "Soldi rimasti: €[soldi]"
                    jump lezione

label lezione:
    scene bg lecturehall
    "..Dopo il pranzo.."
    "* Inizio lezione di Sviluppo di Videogiochi *"
    $ renpy.movie_cutscene("pong.webm")
    show prof
    prof "Allora ragazzi dovete sapere che il pong blablabla"
    prof "ATARI blablabla"
    prof "VIDEOGIOCHI blablabla"
    prof "DOVRETE IMPLEMENTARE UNA TRENTINA DI ROBE CIAO"
    hide prof
    show aci sad
    aci "Che noia queste lezioni sul pong..."
    show aci surprised
    aci "e poi come diamine si progetta un' IA?"
    aci "Io non ho manco capito cosa sono queste 'collisioni' di cui parla..."
    show aci normal
    aci "Hey senti, mi domandavo... vorresti fare il progetto insieme a me?"
    menu:
        "SI, certo":
            call love_increased from _call_love_increased_5
            call friendship_increased from _call_friendship_increased_3
            show aci giggle
            aci "Davvero? Dai, mettiamoci subito all'opera!"
            "Amore +1"
            "Amicizia +1"

        "Veramente mi trovo meglio a lavorare per conto mio":
            show aci surprised
            call hate_increased from _call_hate_increased_9
            call hate_increased from _call_hate_increased_10
            call hate_increased from _call_hate_increased_11
            aci "Non ti conviene, fare tutto da solo ti renderà l'esame molto più pesante!"
            "Antipatia +3"


label codeTogether:
            hide aci surprised
            with fade
            "* Dopo un'ora e mezza di studio *"
            show aci smile
            aci "Ecco fatto, la prima parte del gioco è pronta!"
            aci "Che aspettiamo? Proviamola subito!"
            jump battle_game_1

label afterGame:
    show screen gameUI
    play music "audio/Solanin.ogg" fadein 1.0 volume 0.5
    scene bg lecturehall
    show aci sad
    aci "Beh.. effettivamente potevamo fare di meglio..."
    aci "...le nostre conoscenze di python lasciano molto a desiderare, non trovi?"
    menu:
        "Si, d'altro canto è anche colpa delle inutili lezioni del prof Panizzi":
            show aci giggle
            aci "Ahahah, hai perfettamente ragione!"
            call friendship_increased from _call_friendship_increased_4
            call friendship_increased from _call_friendship_increased_5
            "Amicizia +2"

        "Io credo che tu sia bravissimo in python":
            show aci giggle
            aci "Ma dai, è anche merito tuo"
            call love_increased from _call_love_increased_6
            call love_increased from _call_love_increased_7
            "Amore +2"

        "Le mie conoscenze sono eccellenti, piuttosto le tue lasciano molto a desiderare..":
            show aci surprised
            aci "Beh dato che lo hai realizzato con me è anche colpa tua!"
            call hate_increased from _call_hate_increased_12
            call hate_increased from _call_hate_increased_13
            "Antipatia +2"

label eventide:
    scene bg poli night
    show aci normal
    aci "Si è fatto tardi."
    aci "Dato che abitiamo vicino.."
    aci "Facciamo un pezzo di strada insieme?"

label eventideChoice:
    menu:
        "Si -- (Costo: 1 punti Esse)":
            call checkEssePoints from _call_checkEssePoints_4
            if breaker == False:
                jump eventideChoice
            else:
                show aci giggle
                call love_increased from _call_love_increased_8
                aci "Che belloo!"
                "Amore +1"

                label walk:

                    scene bg street #show aci normal
                    show aci normal
                    aci "Beh da qui in poi ci separiamo"
                    show aci smile
                    aci "A domani!"

        "No":
            show aci angry
            aci "Okay, allora ci vediamo domani."
            call hate_increased from _call_hate_increased_14
            "Antipatia +1"

label home:
    scene bg brn
    "Sei a casa"
    #Suono notifica
    stop music fadeout 1.0
    play music "audio/ringtone.mp3" volume 1.0
    #$ cellulare = True




label chiamata:
    "Il telefono squilla"


    menu:
        "Vuoi rispondere?"
        "SI":
            stop music fadeout 1.0
            play music "audio/Solanin.ogg" fadein 1.0 volume 0.5
            jump home_message
        "NO":
            stop music fadeout 1.0
            play music "audio/Solanin.ogg" fadein 1.0 volume 0.5
            $ cellulare = False
            call hate_increased from _call_hate_increased_15
            call hate_increased from _call_hate_increased_16
            "Antipatia +2"
            jump home_2

label home_2:
    scene bg brm
    with fade
    "IL GIORNO SEGUENTE"
    "ORE 10:00"
    with fade
    play audio "audio/message.mp3" volume 1.0
    "driiing"
    show aci phone at right
    aci "SVEGLIAAAAA"
    aci "E' quasi un'ora che ti aspetto!"

label nextDay:

    aci "Dove sei?????????"
    menu:
        "Che ore sono?":
            aci "SONO LE 10:00"
            aci "LE"
            aci "DIE-"
            aci "-CI"
            call hate_increased from _call_hate_increased_17
            "Antipatia +1"

            label arrivo_1:
                scene bg uni
                show aci angry
                aci "Finalmente!"
                scene bg dib
                show aci perplexed
                aci "L'esame è alle porte, mettiamoci sotto!"

        "Arrivoo, sto per strada! -- (Costo: 1 punto Esse)":
            call checkEssePoints from _call_checkEssePoints_1
            if breaker == False:
                jump nextDay

            else:
                aci "Spero per te che sia vero!"

                label arrivo_2:
                    scene bg uni
                    show aci normal
                    aci "Alla fine ce l'hai fatta!"
                    show aci smile
                    aci "L'esame è alle porte, mettiamoci sotto!"

label day_2_morning:
    scene bg uni
    with fade
    "Dopo tre ore di studio"
    show aci normal
    aci "Sto morendo di fameee"
    show aci surprised
    aci "OH NO!"
    aci "Ho dimenticato i soldi a casa"
    show aci sad
    aci "Ed oggi non ho tessere della mensa"

label day_2_lunch:
    menu:
        "Tranquillo, oggi ti campo io \n (Costo per sfamarlo tutta la giornata: €10)":
            if soldi < 10:
                "Soldi insufficienti"
                jump day_2_lunch

            else:
                show aci normal
                $ richiesta += 1
                if richiesta < 3:
                    aci "No, non posso accettare"
                    jump day_2_lunch
                else:
                    show aci smile
                    aci "Beh, per educazione rifiuto, ma alla terza volta accetto sempre"
                    show aci giggle
                    aci "Lo sai che ti adoro?"
                    call bigMoney_decreased from _call_bigMoney_decreased
                    call love_increased from _call_love_increased_9
                    call love_increased from _call_love_increased_10
                    call friendship_increased from _call_friendship_increased_6
                    call friendship_increased from _call_friendship_increased_7
                    "Costo del pranzo: €10"
                    "Soldi rimasti: €[soldi]"
                    "Amore +2"
                    "Amicizia +2"

        "Se vuoi possiamo dividere il mio pranzo":
            show aci smile
            aci "Davveroo??"
            aci "Grazieee"
            call friendship_increased from _call_friendship_increased_8
            "Amicizia +1"

        "Mi dispiace":
            show aci normal
            aci "Non preoccuparti, scroccherò qualcosa in giro"


label day_2_afternoon:
    hide aci %s
    with fade
    "... Dopo pranzo ..."
    scene bg uni
    show aci normal
    aci "Sono contento che oggi non ci sia lezione"
    show aci smile
    aci "Possiamo ultimare le ultime modifiche al nostro videogame"
    scene bg lecturehall
    show aci normal
    aci "Mentre aggiusto la documentazione ti andrebbe di committare l'ultima issue su 6itHub?"
    menu:
        "Nessun problema":
            show aci smile
            aci "Sapevo di poter contare su di te!"
            call friendship_increased from _call_friendship_increased_9
            "Amicizia +1"

        "Che?":
            show aci surprised
            aci "Ma come?"
            aci "Non sai usare 6it?"
            call hate_increased from _call_hate_increased_18
            "Antipatia +1"

        "Non preoccuparti, l'ho già fatto":
            show aci surprised
            aci "Davvero?"
            if antipatia > 2:
                show aci angry
                aci "Hey!"
                aci "Hai fatto il merge auto-approvando la tua pull request!"
                call hate_increased from _call_hate_increased_19
                "Antipatia +1"
            else:
                show aci smile
                "Ottimo!"
                call friendship_increased from _call_friendship_increased_10
                call friendship_increased from _call_friendship_increased_11
                "Amicizia +2"

label day_2_eventide:
    scene bg dib2
    with fade
    show aci normal
    aci "Documentazione pronta"
    show aci smile
    aci "Codice su 6itHub"
    show aci giggle
    aci "Direi che siamo pronti per questo esame!"

label day_2_eventideChoice:
    menu:
        "Si! Spacchiamolo! -- (Costo 1 punto Esse)":
            call checkEssePoints from _call_checkEssePoints_2
            if breaker == False:
                jump day_2_eventideChoice

            show aci smile
            aci "Così ti voglio!"
            call friendship_increased from _call_friendship_increased_12
            "Amicizia +1"

        "Devo ancora studiare la teoria":
            show aci smile
            aci "Pensi che io l'abbia studiata?"
            show aci giggle
            aci "La studieremo insieme domani!"
            call love_increased from _call_love_increased_11
            "Amore +1"


    show aci surprised
    with fade
    aci "Ci siamo dimenticati di compilare il documento di game design!!!"
    show aci smile
    aci "Dai facciamolo ora al volo, ci metteremo pochi minuti, tanto figurati se il prof lo controlla!"

    scene bg lecturehall
    show aci sad
    with fade
    aci "Accidenti!"
    aci "Questa roba è più lunga e dettagliata del previsto!"
    menu:
        "Dai, concentriamoci e facciamo del nostro meglio":
            show aci normal
            aci "Anche se sembra una frase fatta hai ragione"
            call friendship_increased from _call_friendship_increased_13
            "Amicizia +1"

        "Non ti preoccupare, me ne occupo io!":
            show aci normal
            aci "Siamo una squadra, dobbiamo fare tutto insieme!"
            call friendship_increased from _call_friendship_increased_14
            "Amicizia +1"

        "Scopiazziamola da un altro gruppo":
            show aci smile
            aci "Apprezzo la malvagità, ma sembra che questo pippottone non si possa copiare!"
            show aci giggle
            aci "Ogni gioco è diverso dall'altro."
            call love_increased from _call_love_increased_12
            "Amore +1"

        "Scriviamo cose a caso, l'importante è sembrare che abbiamo combinato qualcosa":
            show aci angry
            aci "Ma non è nel mio stile!"
            call hate_increased from _call_hate_increased_20
            "Antipatia +1"

    show aci normal
    aci "Siamo alle solite.."
    show aci smile
    aci "L'esame è domani e noi stiamo ancora finendo il documento di game design."
    if amore > 9:
        show aci giggle
        aci "Però mi sto divertendo un sacco a studiare con te.."
    else:
        show aci normal
        aci "Non cambieremo mai.."

    "* Dopo un litigio per perfezionare il documento *"

    scene bg poli night
    show aci normal
    with fade
    aci "Domani è il grande giorno.."
    show aci giggle

label day2_night:
    aci "Ansia?"
    menu:
        "Nahhh, ce la caveremo anche a sto giro (costo 1 Punto Esse)":
            call checkEssePoints from _call_checkEssePoints_3
            if breaker == False:
                jump day2_night

            show aci smile
            aci "Ne sono sicuro!"
            call friendship_increased from _call_friendship_increased_15
            "Amicizia +1"

        "Nahhh":
            show aci sad
            aci "Che invidia, io ho paurissima"

        "Siiii":
            show aci sad
            aci "MAR{w}ONN"

    show aci normal
    with fade
    if amore > 9 and amicizia > 5:
        aci "Oggi sto con la macchina.."
        show aci giggle
        aci "Ti do uno strappo a casa!"
        menu:
            "Okay, grazie mille":
                show aci smile
                aci "Figurati"
                aci "Nessun problema"
                call love_increased from _call_love_increased_13
                "Amore +1"

            "Non preoccuparti, vado a piedi":
                show aci sad
                aci "Come preferisci"
                call hate_increased from _call_hate_increased_21
                "Antipatia +3"

label day2_home:
    scene bg brn
    with fade
    "* Sei a casa *"
    "E' ora di dormire"

label day3_morning:
    scene bg brm
    with fade
    "..Oggi è il grande giorno.."
    scene bg dib2
    with fade
    show aci normal
    menu:
        "Buongiorno":
            show aci angry
            aci "Buongiorno un cazzo!"
            call friendship_increased from _call_friendship_increased_16
            "Amicizia +1"

        "Ciao Aciiii!":
            show aci sad
            "Ciao"

    show aci normal
    aci "Oggi ci umilieremo presentando il nostro progetto.."
    show aci smile
    aci "Dai, sono sicuro che andrà bene!"

    scene bg lecturehall
    show prof
    with fade
    prof "Alla luce di ciò che ho constatato"
    prof "il vostro ridicolo progetto è"
    hide prof
    show aci sad
    aci ".."
    hide aci sad
    show prof
    prof "F A N T A S T I C O"
    hide prof
    show aci surprised
    aci "?!"
    hide aci surprised
    show prof
    prof "Mi sono divertito molto a giocare con questa robaccia!"
    if amore >= amicizia and amore > antipatia:
        prof "30!"
        hide prof
        show aci giggle
        aci "UOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOH"
    else:
        prof "28"
        hide prof
        show aci giggle
        aci "Siiii!"

    aci "Te l'avevo detto che ce l'avremmo fatta!"

label day3_eventide:
    scene bg uni
    show aci normal
    with fade
    aci "Beh anche sta volta ce l'abbiamo fatta"
    aci "Abbiamo passato molto tempo insieme durante questo progetto.."

label pre_ending:
    if amore >= amicizia and amore >= antipatia:
        show aci smile
        aci "..."
        show aci giggle
        aci "Credo di essermi innamorato di te"
        jump love_ending

    elif amicizia > amore and amicizia >= antipatia:
        show aci smile
        aci "Saremo amici per sempre!"
        jump friendship_ending

    elif antipatia > amore and antipatia > amicizia:
        show aci perplexed
        aci "Ci si becca..."
        jump bad_ending

label love_ending:
    stop music fadeout 1.0
    play music "audio/lending.mp3" fadein 1.0 volume 0.5
    scene bg lending
    with fade
    show aci giggle
    "FINALE:{w} {color=#f00}Love Ending{/color}"
    "Complimenti"
    "Obiettivo raggiunto!"
    "Aci si è innamorato di te!"

    jump common_ending

label friendship_ending:
    stop music fadeout 1.0
    play music "audio/fending.mp3" fadein 1.0 volume 0.5
    scene bg fending
    with fade
    show aci smile
    "FINALE:{w} {color=#00ff00}Friendship Ending{/color}"
    "Purtroppo Aci non si è innamorato di te.."
    "Ma resterete comunque ottimi amici!"
    jump common_ending

label bad_ending:
    stop music fadeout 1.0
    play music "audio/bending.mp3" fadein 1.0 volume 0.5
    scene bg bending
    with fade
    show aci surprised
    "FINALE:{w} {color=#0000ffff}Bad Ending{/color}"
    "L'antipatia che Aci prova per te è tale da non considerarti una persona a lui cara."
    "Obiettivo fallito."
    jump common_ending

label common_ending:
    "Grazie per aver giocato a Date With Aci"
    "Sviluppatore: {color=#0000ffff}Andrea Scalzo{/color}"
    "Personaggio Aci disegnato da: {color=#f00}Micaela Volpicella{/color}"
    "THE END {w}?"
    return










return
