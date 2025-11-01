import os
os.system("echo \033[1;1H")
os.system("echo \033[2J")
import curses
from curses import wrapper
# from src.klotz import Klotz
from src.cluster import Cluster
from src.tetris_rand import Boden
from src.tetris_rand import Wand
from src.cluster import Formen

stdscr = curses.initscr()

class Game: pass

def main(stdscr):
    # Bildschirm
    stdscr.clear()
    # screen_height, screen_width = stdscr.getmaxyx() // not used
    x = 50 # Startpunkt
    y = 0 # Startpunkt
    screen_width = 119 # screen_width (max 120)
    screen_height = 29 # screen_height (max 30)

    # Klotz
    #klotz = Klotz()
    

    boden = Boden(screen_width, screen_height, 0)
    wand_L = Wand(screen_height, 0, 0)
    wand_R = Wand(screen_height, 0, 119)
    cluster = Cluster()

    while True:
        stdscr.clear()
        
        boden.draw(stdscr.addstr, '=')
        wand_L.draw(stdscr.addstr, '|\n')

        wand_R.draw_Rechts(stdscr.addstr, '|')

        # klotz.draw(stdscr) # jede Zeile des Klotzes wird ausgegeben
        cluster.waehleForm(Formen.T)
        cluster.setForm()
        cluster.drawCluster(stdscr)
        
        # stdscr.addstr(8, 10, str(cluster.get_Seite('L')))
        #stdscr.refresh()
        # stdscr.addstr(9, 10, str(wand_R.get_x()))
        bewegbare_cluster = cluster # Jeder neu erzeugte Cluster, der dem Variable 'bewegbare_cluster' zugewiesen bekommt, darf nur durch diese Zuweisung bewegt werden

        key = stdscr.getch()
        if key == ord('q'):
            break
        if key == curses.KEY_UP and y > 0:
            y -= 1

        if boden.check_ifCollide_Boden(cluster.get_Seite('U')) == False:
            if key == curses.KEY_DOWN: y += 1
        else: # Cluster haftet am Boden und kann nicht mehr bewegt werden, der Cluster wird von diesem Variable entfernt 
            bewegbare_cluster = None

        if wand_R.check_ifCollide_Wand(cluster.get_Seite('R')) == False:
            if key == curses.KEY_RIGHT: x += 1
        else: print('Kollide')

        if wand_L.check_ifCollide_Wand(cluster.get_Seite('L')) == False:
            if key == curses.KEY_LEFT: x -= 1

        if bewegbare_cluster != None:
            bewegbare_cluster.setPos(y,x)
        
curses.wrapper(main)