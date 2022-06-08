label checkEssePoints:
        if puntiEsse < 1:
            $ breaker = False
            "Punti Esse insufficienti"
        else:
            $ puntiEsse -= 1
            "Costo della scelta: 1 punto Esse"
            "Punti Esse rimasti: [puntiEsse]"
            #$ breaker = True
