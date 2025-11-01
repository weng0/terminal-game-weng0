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