from src.cluster import Cluster

class ClusterFest:
    def __init__(self):
        self.unbewegbare_clusters : Cluster = []

    def draw(self, fn_stdscr):
        for c in self.unbewegbare_clusters:
            c.drawCluster(fn_stdscr)

    def get_O_Seiten(self):
        oberseiten = []
        for c in self.unbewegbare_clusters:
            oberseiten += c.get_Seite('O')
        return oberseiten  # = Liste mit aller Oberseiten der Klötze, die in den festsitzenden Cluster vorhanden sind
            # das ist [(y,x), (y,x), ...]
            
    def kollidiert_m_Cluster(self, obj_cluster_pos_u : list):
        kollidiert = False
        oberseiten = self.get_O_Seiten() # das ist [(y,x), (y,x), ...]

        if len(oberseiten) > 3:pass
        for pos_u in obj_cluster_pos_u:
            y_u, x_u = pos_u
            for pos_o in oberseiten:
                y_o, x_o = pos_o

                if y_u+1 == y_o and x_u == x_o:
                    kollidiert = True
                    print('Kollidiert')
        return kollidiert