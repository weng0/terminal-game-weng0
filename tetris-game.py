import os
os.system("echo \033[1;1H")
os.system("echo \033[2J")
import curses
from curses import wrapper

class Game: pass

class Klotz:
    def __init__(self):
        self.x_pos = 0
        self.y_pos = 0

    def getUnterseite(self):
        y_pos_u = self.y_pos+2
        return y_pos_u

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
    
class Tetris_Rand:
    def __init__(self, mul, y, x):
        self.x_pos = x
        self.y_pos = y
        self.rand = "="*mul
    
    def get_x(self):
        return self.x_pos
    
    def get_y(self):
        return self.y_pos
    
    def draw_Rand(self, stdscr_fn):
        stdscr_fn(self.y_pos, self.x_pos, self.rand)

class Boden(Tetris_Rand):
    def __init__(self, mul, y, x):
        super().__init__(mul, y, x)

    # Kollidieren: Bitte ausbessern
    def check_ifCollide_Boden(self, fn_obj_unten): # fn_obj2_pos = z.B. Wand
        collide = False
        #y_1 = fn_obj1_unten # hier unten // not used
        #y_2 = fn_boden_pos             // not used
        if fn_obj_unten+1 == self.y_pos:
            collide = True
        return collide

class Wand(Tetris_Rand):
    def __init__(self, mul, y, x):
        super().__init__(mul, y, x)


def main(stdscr):
    # Bildschirm
    stdscr.clear()
    # screen_height, screen_width = stdscr.getmaxyx() // not used
    x = 0 # Startpunkt
    y = 0 # Startpunkt
    screen_width = 118 # screen_width (max 120)
    screen_height = 29 # screen_height (max 30)
    # Klotz
    klotz = Klotz()
    klotz_draw = klotz.draw_Klotz()
    boden = Boden(screen_width, screen_height, 0)
    wand_L = Wand(screen_height, 0, 0)
    wand_R = Wand(screen_height, 0, screen_width)

    while True:
        stdscr.clear()
        #stdscr.addstr(wand.draw_Boden())
        boden.draw_Rand(stdscr.addstr)

        for i in range(len(klotz_draw)):
            line = klotz_draw[i]
            stdscr.addstr(y+i, x, line) # je Zeile des Klotzes wird ausgegeben
        
        stdscr.addstr(10, 10, 'Kollidiert nicht')
        stdscr.addstr(8, 10, str(klotz.getUnterseite()))
        #stdscr.refresh()
        key = stdscr.getch()
        if key == ord('q'):
            break
        if key == curses.KEY_UP and y > 0:
            y -= 1

        if boden.check_ifCollide_Boden(klotz.getUnterseite()) == False:
            if key == curses.KEY_DOWN and y < 29:
                y += 1

        if key == curses.KEY_RIGHT and x < 118: x += 1
        if key == curses.KEY_LEFT and x > 0: x -= 1
        klotz.setPos(y,x)
curses.wrapper(main)