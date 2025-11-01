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
    
    # def kollidiert_m_Cluster(self, obj_cluster_pos_u : list):
    #     kollidiert = False
    #     oberseiten = self.get_O_Seiten() # Liste
    #     for pos_u in obj_cluster_pos_u:
    #         for pos_o in oberseiten:
    #             if pos_u == pos_o:
    #                 kollidiert = True
    #                 print('Kollidiert')
    #     return kollidiert