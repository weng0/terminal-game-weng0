from src.cluster import Cluster
from src.klotz import Klotz

class ClusterFest:
    def __init__(self, screen_height, screen_width):
        self.unbewegbare_clusters : Cluster = []
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.y_schritte = int(screen_height/2)
        self.x_schritte = int((screen_width-1)/3)
        self.koordinatensys = None
        self.alle_kloetze = None

    # def draw(self, fn_stdscr):
    #     for c in self.unbewegbare_clusters:
    #         c.drawCluster(fn_stdscr)

    def draw(self, fn_stdscr):
        if self.alle_kloetze != None:
            for k in self.alle_kloetze:
                k.draw(fn_stdscr)

    def get_Seiten(self, seite : str):
        oberseiten = []
        for c in self.unbewegbare_clusters:
            if seite == 'O':
                oberseiten += c.get_Seite('O')
            if seite == 'R':
                oberseiten += c.get_Seite('R')
            if seite == 'L':
                oberseiten += c.get_Seite('L')
            
        return oberseiten  # = Liste mit aller Oberseiten der Klötze, die in den festsitzenden Cluster vorhanden sind
            # das ist [(y,x), (y,x), ...]

    def kollidiert_oben(self, obj_cluster_pos_u : list):
        kollidiert = False
        oberseiten = self.get_Seiten('O') # das ist [(y,x), (y,x), ...]

        for pos_u in obj_cluster_pos_u:
            y_u, x_u = pos_u
            for pos_o in oberseiten:
                y_o, x_o = pos_o

                if y_u+1 == y_o and x_u == x_o:
                    kollidiert = True
        return kollidiert
    
    def kollidiert_seitlich(self, cluster_R_or_L : list, get_R_or_L : str): # Wenn Cluster_R -> Fest_L / Fest_R <- Cluster_L
        kollidiert = False
        feste_seiten = None
        if get_R_or_L == 'R':
            feste_seiten = self.get_Seiten('R') # das ist [(y,x), (y,x), ...]
        if get_R_or_L == 'L':
            feste_seiten = self.get_Seiten('L')

        for cluster_pos in cluster_R_or_L:
            cluster_y, cluster_x = cluster_pos
            for pos_fest in feste_seiten:
                y_fest, x_fest = pos_fest

                if cluster_y == y_fest and x_fest == cluster_x-1: # Fest_R <- Cluster_L
                    kollidiert = True
                if cluster_y == y_fest and cluster_x+1 == x_fest: # Cluster_R -> Fest_L
                    kollidiert = True
        return kollidiert
    
    def screen_koordinatensystem(self):
        # creat screen_blocks
        screen_blocks = []
        for ys in range(self.y_schritte):
            screen_blocks.append([])
            #for xs in range(self.x_schritte): 
                #screen_blocks[ys].append('-') # '-' ist hier nur platzhalter bitter ersetzen !!!
        # print(screen_blocks) funkt
        return screen_blocks
    
    def kloetze_neu_anordnen(self):
        self.koordinatensys = self.screen_koordinatensystem()
        alle_kloetze = []
        for uc in self.unbewegbare_clusters:
            for k in uc.get_Kloetze():
                alle_kloetze.append(k)
        #print(len(alle_kloetze)) funkt

        h = self.screen_height
        while h > 0:
            for zeile in self.koordinatensys:
                #print('h:', h
                
                #for elem in range(len(zeile)):
                w = 1
                found = True
                while w < self.screen_width-1:
                    #print('w:', w)
                    for k in alle_kloetze:
                        if h == k.get_y() and w == k.get_x():
                            #elem = k.get_y(), k.get_x()
                            zeile.append(k)
                            found = True
                            break
                        else: found = False
                    if found == False:
                        zeile.append('-')
                    w+= 3
                h -= 2
                #print('h:', h)
        if len(alle_kloetze) > 0:pass
            #print(self.koordinatensys)
        self.alle_kloetze = alle_kloetze

    def delete(self):
        verschiebung = 0
        h = self.screen_height
        while h > 0:
            #w = 1
            
            #while w < self.screen_width-1:
            for zeile in self.koordinatensys:
                align = []
                for elem in zeile:
                #print(zeile)
                    if elem != '-':
                        if elem.get_y() == h:
                            align.append(elem)
                #print(len(align))
                if len(align) == self.x_schritte:
                    verschiebung += 1
                    for a in align:
                        k = len(self.alle_kloetze)-1
                        while k > 0:
                        #for k in len(self.alle_kloetze):
                            # klotz = self.alle_kloetze[k]
                            # if klotz.get_y() == a.get_y():
                            #     del self.alle_kloetze[k]
                            klotz = self.alle_kloetze[k]
                            print(k-1)
                            if klotz.get_y() == a.get_y():
                                del self.alle_kloetze[k]
                            k-= 1

                    # k_range = 
                    # while k_range > 0:
                    #     if self.alle_kloetze[k_range].get_y() == h:
                    #         del self.alle_kloetze[k_range]
                    #         k -= 1
                h -= 2
        ## Verschiebung
        for k in self.alle_kloetze:
            y = k.get_y() + verschiebung*2
            k.set_y(y)