class Klotz:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0

    def getUnterseite(self):
        return self.y_pos+2
    
    def get_R_Seite(self):
        return self.x_pos+5
    
    def get_L_Seite(self):
        return self.x_pos

    def setPos(self, y, x):
        self.y_pos = y
        self.x_pos = x

    def getPos(self):
        return self.y_pos, self.x_pos
    
    def draw_Klotz(self):
        l1 = '######'
        l2 = '#    #'
        l3 = '######'
        lines = [l1, l2, l3]
        return lines