################################################################################
## Inizializzazione
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Dichiarare gui.init resetta gli stili ai valori predefiniti, e imposta
## l'altezza e larghezza del gioco.
init python:
    gui.init(1280, 720)



################################################################################
## Variabili di Configurazione GUI
################################################################################


## Colori ######################################################################
##
## I colori del testo nell'interfaccia.

## Un colore di risalto usato nell'interfaccia per le etichette e il testo in
## evidenza.
define gui.accent_color = u'#9933ff'

## Il colore usato per il testo di un pulsante quando non è nè selezionato nè
## sotto il puntatore.
define gui.idle_color = u'#5F3329' #prima era #888888

## Il colore small è usato per testo piccolo, che richiede di essere più chiaro
## o più scuro per ottenere lo stesso effetto.
define gui.idle_small_color = u'#aaaaaa'

## Il colore usato per pulsanti e barre che si trovano sotto il puntatore.
define gui.hover_color = u'#c184ff' #prima era #c184ff

## Il colore usato per il testo di un pulsante che è selezionato ma non
## evidenziato. Un pulsante è selezionato se indica l'attuale schermata o valore
## di preferenza.
define gui.selected_color = u'#ffffff'

## Il colore del testo per un pulsante che non può venire selezionato.
define gui.insensitive_color = u'#8888887f'

## Colori usati per le frazioni di barre che non sono riempite. Non vengono
## usati direttamente, ma lo sono quando si ri-generano i file immagine della
## barra.
define gui.muted_color = u'#3d1466'
define gui.hover_muted_color = u'#5b1e99'

## I colori usati per il dialogo e le scelte.
define gui.text_color = u'#ffffff'
define gui.interface_text_color = u'#ffffff'


## Font e Dimensioni ###########################################################

## Il font usato per il testo interno al gioco.
define gui.text_font = "fonts/Bryndan_Write.ttf"

## Il font usato per i nomi dei personaggi.
define gui.name_text_font = "fonts/Bryndan_Write.ttf"

## Il font usato per il testo esterno al gioco.
define gui.interface_text_font = "fonts/Bryndan_Write.ttf"

## La dimensione del normale testo di dialogo.
define gui.text_size = 28

## La dimensione dei nomi dei personaggi.
define gui.name_text_size = 35

## Le dimensioni del testo nell'interfaccia di gioco.
define gui.interface_text_size = 40

## Le dimensioni delle etichette nell'interfaccia di gioco.
define gui.label_text_size = 24

## La dimensione del testo delle notifiche (notify screen).
define gui.notify_text_size = 16

## Le dimensioni del titolo del gioco.
define gui.title_text_size = 50


## Menu - Main e Game ##########################################################

## Le immagini usate per i menu Main e Game.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialogo #####################################################################
##
## Queste variabili controllano come viene mostrato il dialogo a schermo una
## linea alla volta.

## L'altezza del textbox contenente il dialogo.
define gui.textbox_height = 185

## La posizione verticale del textbox sullo schermo. 0.0 è in alto, 0.5 è al
## centro, e 1.0 è in basso.
define gui.textbox_yalign = 1.0


## La posizione del nome del personaggio, relativa al textbox. Può essere un
## numero esatto di pixel da sinistra o da sopra, oppure 0.5 per centrare.
define gui.name_xpos = 240
define gui.name_ypos = 0

## L'allineamento orizzontale del nome del personaggio. Può essere 0.0 per
## allinearlo a sinistra, 0.5 al centro e 1.0 a destra.
define gui.name_xalign = 0.0

## Larghezza, altezza e bordi del riquadro che contiene il nome del personaggio,
## oppure None per dimensionarlo automaticamente.
define gui.namebox_width = None
define gui.namebox_height = None

## I bordi del riquadro che contiene il nome del personaggio, in questo ordine:
## sinistro, superiore, destro, inferiore.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Se 'True', lo sfondo di namebox sarà tassellato (ripetuto come una
## piastrella). Se 'False' sarà invece scalato.
define gui.namebox_tile = False


## La posizione dei dialoghi, relativa al textbox. Può essere un numero esatto
## di pixel relativo ai bordi sinistro o superiore del textbox, oppure 0.5 per
## centrare.
define gui.dialogue_xpos = 268
define gui.dialogue_ypos = 50

## La larghezza massima del testo di dialogo, in pixel.
define gui.dialogue_width = 744

## L'allineamento orizzontale del testo di dialogo. Può essere 0.0 per
## allinearlo a sinistra, 0.5 al centro e 1.0 a destra.
define gui.dialogue_text_xalign = 0.0


## Pulsanti ####################################################################
##
## Queste variabili, assieme alle immagini contenute in gui/button, definiscono
## l'aspetto dei pulsanti.

## Larghezza e altezza di un pulsante, in pixel. Se 'None', Ren'Py calcolerà una
## dimensione.
define gui.button_width = None
define gui.button_height = None

## I bordi su ogni lato del pulsante, nell'ordine: sinistro, superiore, destro,
## inferiore.
define gui.button_borders = Borders(4, 4, 4, 4)

## Se 'True', l'immagine di sfondo sarà tassellata. Se 'False', l'immagine di
## sfondo verrà scalata.
define gui.button_tile = False

## Il font usato dal pulsante.
define gui.button_text_font = gui.interface_text_font

## La dimensione del testo usato dal pulsante.
define gui.button_text_size = gui.interface_text_size

## Colore testo nel pulsante, secondo i vari stati.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## L'allineamento orizzontale del testo nel pulsante. (0.1 a sinistra, 0.5 al
## centro, 1.0 a destra).
define gui.button_text_xalign = 0.0


## Queste variabili sovrascrivono le impostazioni per differenti tipi di
## pulsante. Leggere nella documentazione i tipi di pulsante disponibili, e per
## cosa viene usato ciascuno.
##
## Queste personalizzazioni sono usate dall'interfaccia predefinita:

define gui.radio_button_borders = Borders(18, 4, 4, 4)

define gui.check_button_borders = Borders(18, 4, 4, 4)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(10, 4, 10, 4)

define gui.quick_button_borders = Borders(10, 4, 10, 0)
define gui.quick_button_text_size = 14
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Puoi aggiungere le tue personalizzazioni, aggiungendo variabili con la giusta
## nomenclatura. Per esempio, puoi togliere il segno # dalla linea seguente per
## impostare una larghezza fissa dei pulsanti di navigazione.

# define gui.navigation_button_width = 250


## Pulsanti Scelta #############################################################
##
## I pulsanti di scelta sono usati per i menu interni al gioco.

define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(100, 5, 100, 5)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#444444"


## Pulsanti Slot ###############################################################
##
## Un pulsante Slot è un tipo di pulsante speciale. Contiene un'immagine
## miniatura, e testo che riporta i contenuti dello slot. Uno Slot Save usa
## immagini presenti in gui/button, come tutti gli altri tipi di pulsante.

## Il pulsante slot.
define gui.slot_button_width = 276
define gui.slot_button_height = 206
define gui.slot_button_borders = Borders(10, 10, 10, 10)
define gui.slot_button_text_size = 14
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Larghezza e altezza delle miniature usate dallo slot.
define config.thumbnail_width = 256
define config.thumbnail_height = 144

## Numero di colonne e righe della griglia degli slot.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Posizioni e Spaziature ######################################################
##
## Queste variabili controllano posizione e spaziatura di vari elementi
## dell'interfaccia.

## Posizione del lato sinistro dei pulsanti di navigazione, relativa al lato
## sinistro dello schermo.
define gui.navigation_xpos = 40

## Posizione verticale dell'indicatore 'SALTO'.
define gui.skip_ypos = 10

## Posizione verticale delle notifiche.
define gui.notify_ypos = 45

## Spaziatura fra le scelte.
define gui.choice_spacing = 22

## Pulsanti nella sezione di navigazione dei menu Main e Game.
define gui.navigation_spacing = 10

## Controlla l'ammontare di spazio fra le opzioni (preferences).
define gui.pref_spacing = 10

## Controlla l'ammontare di spazio fra i pulsanti delle opzioni (preferences).
define gui.pref_button_spacing = 0

## La spaziatura fra i pulsanti delle pagine file.
define gui.page_spacing = 0

## Spaziatura fra gli slot.
define gui.slot_spacing = 10

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Frame #######################################################################
##
## Queste variabili controllano l'aspetto dei frame che possono contenere
## elementi d'interfaccia quando un livello sostrato (overlay) o una finestra
## sono assenti.

## Generic frames.
define gui.frame_borders = Borders(4, 4, 4, 4)

## Frame usato come parte del confirm screen.
define gui.confirm_frame_borders = Borders(40, 40, 40, 40)

## Frame usato come parte dello skip screen.
define gui.skip_frame_borders = Borders(16, 5, 50, 5)

## Frame usato come parte delle notifiche.
define gui.notify_frame_borders = Borders(16, 5, 40, 5)

## Gli sfondi del frame devono essere tassellati?
define gui.frame_tile = False


## Barre, Barre Scorrimento e Selettori ########################################
##
## Controllano aspetto e dimensioni di barre e selettori
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## Altezza delle barre orizzontali. Larghezza delle barre verticali.
define gui.bar_size = 25
define gui.scrollbar_size = 12
define gui.slider_size = 25

## 'True' se le immagini devono venire tassellate. 'False' se devono venire
## scalate.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Bordi orizzontali.
define gui.bar_borders = Borders(4, 4, 4, 4)
define gui.scrollbar_borders = Borders(4, 4, 4, 4)
define gui.slider_borders = Borders(4, 4, 4, 4)

## Bordi verticali.
define gui.vbar_borders = Borders(4, 4, 4, 4)
define gui.vscrollbar_borders = Borders(4, 4, 4, 4)
define gui.vslider_borders = Borders(4, 4, 4, 4)

## Cosa fare con barre di scorrimento che non possono scorrere. "hide" le
## nasconde, mentre None le mostra comunque.
define gui.unscrollable = "hide"


## History #####################################################################
##
## Lo screen 'History' mostra una cronologia dei dialoghi già letti dal
## giocatore.

## Il numero di blocchi di dialogo conservati da Ren'Py nella cronologia.
define config.history_length = 250

## L'altezza di un elemento nella schermata di cronologia, oppure None per avere
## altezze variabili al costo delle prestazioni.
define gui.history_height = 140

## Posizione, larghezza e allineamento dell'etichetta che equivale al nome del
## personaggio in causa.
define gui.history_name_xpos = 155
define gui.history_name_ypos = 0
define gui.history_name_width = 155
define gui.history_name_xalign = 1.0

## Posizione, larghezza e allineamento del testo di dialogo.
define gui.history_text_xpos = 170
define gui.history_text_ypos = 2
define gui.history_text_width = 740
define gui.history_text_xalign = 0.0


## Modalità NVL ################################################################
##
## Lo screen NVL mostra il dialogo dei personaggi NVL.

## I bordi della finestra in Modalità NVL.
define gui.nvl_borders = Borders(0, 10, 0, 20)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## L'altezza di un elemento NVL. Impostalo a 'None' e gli elementi stabiliranno
## un'altezza automatica.
define gui.nvl_height = 115

## La spaziatura fra gli elementi in Modalità NVL, quando gui.nvl_height è None,
## e fra questi e un menu NVL.
define gui.nvl_spacing = 10

## Posizione, larghezza e allineamento dell'etichetta che equivale al nome del
## personaggio in causa.
define gui.nvl_name_xpos = 430
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 150
define gui.nvl_name_xalign = 1.0

## Posizione, larghezza e allineamento del testo di dialogo.
define gui.nvl_text_xpos = 450
define gui.nvl_text_ypos = 8
define gui.nvl_text_width = 590
define gui.nvl_text_xalign = 0.0

## La posizione, larghezza e allineamento del testo nvl_thought (il testo del
## personaggio nvl_narrator.)
define gui.nvl_thought_xpos = 240
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 780
define gui.nvl_thought_xalign = 0.0

## La posizione dei menu_buttons in modalità NVL.
define gui.nvl_button_xpos = 450
define gui.nvl_button_xalign = 0.0

## Localizzazione ##############################################################

## Questo controlla dove avviene un'interruzione di riga. Il valore predefinito
## è valido per la maggior parte dei linguaggi. Una lista di valori disponibili
## si può trovare su:https://www.renpy.org/doc/html/style_properties.html#style-
## property-language

define gui.language = "unicode"


################################################################################
## Dispositivi mobili
################################################################################

init python:

    ## Questo aumenta la dimensione dei Pulsanti Rapidi per renderli più facili
    ## da toccare su tablet e telefoni.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(40, 14, 40, 0)

    ## Questo cambia la dimensione e spaziatura di vari elementi della GUI per
    ## assicurarsi che siano facilmente visibili su telefono.
    @gui.variant
    def small():

        ## Dimensioni font.
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 30
        gui.button_text_size = 30
        gui.label_text_size = 34

        ## Cambia la posizione del textbox.
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.dialogue_xpos = 90
        gui.dialogue_width = 1100

        ## Change the size and spacing of various things.
        gui.slider_size = 36

        gui.choice_button_width = 1240
        gui.choice_button_text_size = 30

        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10

        gui.history_height = 190
        gui.history_text_width = 690

        gui.quick_button_text_size = 20

        ## Schema pulsanti file.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Modalità NVL.
        gui.nvl_height = 170

        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325

        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5

        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20

        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
