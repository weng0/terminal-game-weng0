class Klotz:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0
        self.rows = ['###','###']

    def getZeilenlaenge(self):
        return 3

    def set_y(self, neue_y):
        self.y_pos = neue_y

    def get_x(self):
        return self.x_pos
    
    def get_y(self):
        return self.y_pos

    def getUnterseite(self):
        return self.y_pos+1,self.x_pos
    
    def get_R_Seite(self):
        return self.y_pos, self.x_pos+2
    
    def get_L_Seite(self):
        return self.y_pos, self.x_pos
    
    def get_O_Seite(self):
        return self.y_pos, self.x_pos

    def setPosition(self, y, x):
        self.y_pos = y
        self.x_pos = x

    def getPos(self):
        return self.y_pos, self.x_pos
    
    def draw(self, stdscr_fn):
        for i in range(len(self.rows)):
            line = self.rows[i]
            stdscr_fn.addstr(self.y_pos+i, self.x_pos, line)