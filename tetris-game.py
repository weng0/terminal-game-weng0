import os
os.system("echo \033[1;1H")
os.system("echo \033[2J")
import curses
from curses import wrapper
from src.klotz import Klotz
from src.tetris_rand import Boden
from src.tetris_rand import Wand

class Game: pass

    

def main(stdscr):
    # Bildschirm
    stdscr.clear()
    # screen_height, screen_width = stdscr.getmaxyx() // not used
    x = 0 # Startpunkt
    y = 0 # Startpunkt
    screen_width = 119 # screen_width (max 120)
    screen_height = 29 # screen_height (max 30)
    # Klotz
    klotz = Klotz()
    #klotz_draw = klotz.draw(stdscr)
    boden = Boden(screen_width, screen_height, 0)
    wand_L = Wand(screen_height, 0, 0)
    wand_R = Wand(screen_height, 0, 119)

    while True:
        stdscr.clear()
        #stdscr.addstr(wand.draw_Boden())
        boden.draw(stdscr.addstr, '=')
        wand_L.draw(stdscr.addstr, '|\n')

        wand_R.draw_Rechts(stdscr.addstr, '|') # muss anpassen

        klotz.draw(stdscr) # jede Zeile des Klotzes wird ausgegeben
        
        stdscr.addstr(10, 10, 'Kollidiert nicht')
        stdscr.addstr(8, 10, str(klotz.getUnterseite()))
        #stdscr.refresh()
        key = stdscr.getch()
        if key == ord('q'):
            break
        if key == curses.KEY_UP and y > 0:
            y -= 1

        if boden.check_ifCollide_Boden(klotz.getUnterseite()) == False:
            if key == curses.KEY_DOWN and y < 29: y += 1

        if wand_R.check_ifCollide_Wand(klotz.get_R_Seite()) == False:
            if key == curses.KEY_RIGHT and x < 118: x += 1

        if wand_L.check_ifCollide_Wand(klotz.get_L_Seite()) == False:
            if key == curses.KEY_LEFT and x > 0: x -= 1
        klotz.setPos(y,x)
curses.wrapper(main)