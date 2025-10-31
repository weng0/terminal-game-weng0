class Klotz:
    def __init__(self):
        self.x_pos = 1
        self.y_pos = 0
        self.rows = ['######', '#    #', '######']
        

    def getUnterseite(self):
        return self.y_pos+2
    
    def get_R_Seite(self):
        return self.x_pos+5
    
    def get_L_Seite(self):
        return self.x_pos

    def setDrawPosition(self, y, x):
        self.y_pos = y
        self.x_pos = x

    def getPos(self):
        return self.y_pos, self.x_pos
    
    def draw(self, stdscr_fn):
        for i in range(len(self.rows)):
            line = self.rows[i]
            stdscr_fn.addstr(self.y_pos+i, self.x_pos, line)

import random
random.seed()

class Cluster:
    def __init__(self):
        self.klotz_cluster : Klotz = [Klotz(),Klotz(),Klotz(),Klotz()]
        self.y = 15
        self.x = 50

    def setForm(self):
        y = self.y
        x = self.x
        z = [(x,y),(x+6,y),(x+6,y+3), (x+(6)*2, y+3)]
        for i in range(len(self.klotz_cluster)):
            k = self.klotz_cluster[i]
            x, y = z[i]
            k.setDrawPosition(y,x)

    def drawCluster(self, stdscr_fn):
        for i in self.klotz_cluster:
            i.draw(stdscr_fn)
        
