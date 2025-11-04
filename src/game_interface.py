from src.cluster_fest import ClusterFest

class Game_Interface:
    def __init__(self):
        self.punktzahl = 0
        self.spieler_name = ''
    
    def setName(self): pass#, fn_stdscr pass
        # wort = ''

        # fn_stdscr.addstr(10, 85, 'Bitte geben Sie Ihre Spielername ein')
        # while 
        # buchstabe = input()
        # return self.spieler_name


    def update_Punktzahl(self, cluster_f : ClusterFest):
        self.punktzahl = cluster_f.get_kompleteReihen()

    def print_Interface(self, stdscr_fn):
        stdscr_fn.addstr(10, 55, f"Punktzahl: {self.punktzahl}")