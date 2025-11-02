from src.cluster import Cluster

class ClusterFest:
    def __init__(self):
        self.unbewegbare_clusters : Cluster = []

    def draw(self, fn_stdscr):
        for c in self.unbewegbare_clusters:
            c.drawCluster(fn_stdscr)

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