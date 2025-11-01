class Klotz:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.rows = ['###','###']

    def getUnterseite(self):
        return self.y_pos+1
    
    def get_R_Seite(self):
        return self.x_pos+2
    
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

import enum
class Formen(enum.Enum):
    Z = 1
    L = 2
    I = 3
    T = 4
    O = 5

'''
T:
         (x,y)
(x-3,y+2)(x,y+2)(x+3, y+2)

I:
(x,y)
(x,y+2)
(x,(y+2)*2)
(x,(y+2)*3)

L:
(x,y)
(x,y+2)
(x,(y+2)*2)(x+3,(y+2)*2)

O:
(x,y)(x+3, y)
(x,y+2)(x+3, y+2)
'''

import random
random.seed()
'https://www.geeksforgeeks.org/python/enum-in-python/'
class Cluster:
    def __init__(self):
        self.klotz_cluster : Klotz = [Klotz(),Klotz(),Klotz(),Klotz()]
        self.y = 0
        self.x = 50
        self.form = None

    def waehleForm(self, waehl_form : Formen):
        y = self.y
        x = self.x
        if waehl_form == Formen.Z:
            z = [(x,y),(x+3,y),(x+3,y+2), (x+(3)*2, y+2)]
            self.form = z
        if waehl_form == Formen.I:
            i = [(x,y), (x,y+2), (x,(y+2)*2), (x,(y+2)*3)]
            self.form = i
        if waehl_form == Formen.L:
            l = [(x,y), (x,y+2), (x,(y+2)*2), (x+3,(y+2)*2)]
            self.form = l
        if waehl_form == Formen.O:
            o = [(x,y), (x+3, y), (x,y+2), (x+3, y+2)]
            self.form = o
        if waehl_form == Formen.T:
            t = [(x,y), (x-3,y+2), (x,y+2), (x+3, y+2)]
            self.form = t

    def setForm(self):
        for i in range(len(self.klotz_cluster)):
            k = self.klotz_cluster[i]
            x, y = self.form[i] # !!!
            k.setDrawPosition(y,x)

    def drawCluster(self, stdscr_fn):
        for i in self.klotz_cluster:
            i.draw(stdscr_fn)

    def get_Seite(self, richtung : str): # von allen Klötzen im Cluster // Richtung = z.B. 'R', 'L', 'U'
        x_or_y_pos = []
        for i in self.klotz_cluster:
            if richtung == 'R':
                x_or_y_pos.append(i.get_R_Seite())
            if richtung == 'L':
                x_or_y_pos.append(i.get_L_Seite())
            if richtung == 'U':
                x_or_y_pos.append(i.getUnterseite())
        return x_or_y_pos
        
    def setPos(self, y, x):
        self.y = y
        self.x = x