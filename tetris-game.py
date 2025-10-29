import os
os.system("echo \033[1;1H")
os.system("echo \033[2J")
import curses
from curses import wrapper

class Game: pass

class Klotz:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def draw_Klotz(self):
        l1 = '######'
        l2 = '#    #'
        l3 = '######'
        lines = [l1, l2, l3]
        return lines
    
class Wand:
    def __init__(self, screen_height, screen_width):
        self.x_pos = 0
        self.y_pos = screen_height
        self.boden = "="*screen_width
    
    def draw_Boden(self, stdscr_fn):
        stdscr_fn(self.y_pos, self.x_pos, self.boden)
        #return self.y_pos, self.x_pos, self.boden


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
    wand = Wand(screen_height, screen_width)

    while True:
        stdscr.clear()
        #stdscr.addstr(wand.draw_Boden())
        wand.draw_Boden(stdscr.addstr)
        for i in range(len(klotz_draw)):
            line = klotz_draw[i]
            stdscr.addstr(y+i, x, line) # je Zeile des Klotzes wird ausgegeben
        
        #stdscr.refresh()
        key = stdscr.getch()
        if key == ord('q'):
            break
        if key == curses.KEY_UP and y > 0:
            y -= 1
        if key == curses.KEY_DOWN and y < 29: y += 1
        if key == curses.KEY_RIGHT and x < 118: x += 1
        if key == curses.KEY_LEFT and x > 0: x -= 1

curses.wrapper(main)



