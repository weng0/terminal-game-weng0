class Game_Interface:
    def __init__(self):
        self.punktzahl = 0
        self.spieler_name = ''
    
    def setName(self):
        self.spieler_name = input('Bitte geben Sie Ihre Spielername ein\n-> ')

    def update_Punktzahl(self, punkte):
        self.punktzahl = punkte