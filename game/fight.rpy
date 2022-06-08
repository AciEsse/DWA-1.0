define rospo = Character('Rospo', color="#00cc00")
define borghese = Character('Borghese', color="#CD0000")

screen simple_stats_screen:
    frame:
        xalign 0.01 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Rospo" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value rospo_hp
                    range rospo_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[rospo_hp] / [rospo_max_hp]" size 16


    frame:
        xalign 0.99 yalign 0.05
        xminimum 220 xmaximum 220
        vbox:
            text "Borghese" size 22 xalign 0.5
            null height 5
            hbox:
                bar:
                    xmaximum 130
                    value borghese_hp
                    range borghese_max_hp
                    left_gutter 0
                    right_gutter 0
                    thumb None
                    thumb_shadow None

                null width 5

                text "[borghese_hp] / [borghese_max_hp]" size 16

    text "Rospo vs. Borghese" xalign 0.5 yalign 0.05 size 30

# The game starts here.
label battle_game_1:
    hide screen gameUI
    hide screen bagUI
    stop music fadeout 1.0
    #play audio "audio/Ci siamo.mp3" volume 13.0
    play music "audio/Battle Theme.mp3" fadein 1.0 volume 0.4
    #### Some variables that describes the game state.
    $ borghese_max_hp = 30
    $ rospo_max_hp = 50
    $ borghese_hp = borghese_max_hp
    $ rospo_hp = rospo_max_hp
    $ cookies_left = 13

    scene bg fight

    "C'era una volta un rospo magico in grado di sputare monete d'oro in cambio di biscotti."
    "Un giorno mostrò i suoi poteri in un villaggio molto povero."
    "Gli abitanti del villaggio rimasero affascinati dai poteri del rospo magico, al punto da stipulare un patto."
    "Ogni giorno il rospo avrebbe ricevuto cento biscotti al suo risveglio, ed in cambio lui avrebbe regalato ad ogni abitante 100 monete d'oro."
    play audio "audio/Ci siamo.mp3" volume 13.0
    "Un giorno, uno spietato borghese decise di rapire il rospo per diventare abbastanza ricco da potersi permettere un bilocale a 'Poggiofranco'."
    "Il rospo magico era troppo viscido per essere catturato, continuava a scivolare via dalle grinfie dell'avido borghese."
    "Il rapitore allora decise di estrarre la sua spada, {w}e a quel punto..."
    jump battle_1_loop


label battle_1_loop:

    #### Let's show the game screen.
    #
    show screen simple_stats_screen

    #### The game loop.
    # It will exist till both enemies have more than 0 hp.
    #
    while (borghese_hp > 0) and (rospo_hp > 0):

        menu:
            "Attacca":
                $ borghese_hp -= 2
                play audio "audio/frog punch.ogg" volume 1.0
                rospo "K-y-aaa!!! (Danno Inflitto: 2)"

            "Mangia un biscotto (biscotti rimasti: [cookies_left])" if cookies_left > 0:
                $ rospo_hp = min(rospo_hp+5, rospo_max_hp)
                $ cookies_left -= 1
                play audio "audio/munch sound.ogg" volume 1.0
                rospo "Mmm, squisiti!... (hp Rigenerati: 5)"

        $ borghese_damage = renpy.random.randint(1, 6)
        play audio "audio/sword sound.mp3" volume 1.0

        $ rospo_hp -= borghese_damage

        borghese "RrrrrRRrrrr! {i}Prendi questooo!{/i} (Danno inflitto: [borghese_damage])"
    #
    ####

    hide screen simple_stats_screen

    if borghese_hp <= 0:
        if rospo_hp <= 0:
            "* Prima di morire il nemico lancia la sua spada... *"
            "Doppio KO"

        else:
            play audio "audio/win sound.ogg" volume 1.0
            rospo "Ho vinto!"
            rospo "Finalmente potrò tornare al villaggio!"
            rospo "Mi sono rimasti solo [cookies_left] biscotti"

    else:
        borghese "Ah-Ah-Ah {i}Cosa credevi di fare?{/i}  * accarezza la spada *"

    jump battle_1_ending

label battle_1_ending:
    "Fine"
    stop music fadeout 1.0
    jump afterGame
    #return
