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
import random
random.seed()
stdscr = curses.initscr()

class TetrisGame: pass

def main(stdscr):
    # Bildschirm
    stdscr.clear()
    # screen_height, screen_width = stdscr.getmaxyx() // not used
    x = 50 # Startpunkt
    y = 0 # Startpunkt
    screen_width = 119 # screen_width (max 120)
    screen_height = 29 # screen_height (max 30)
    unbewegbare_clusters : Cluster = []
    boden = Boden(screen_width, screen_height, 0)
    wand_L = Wand(screen_height, 0, 0)
    wand_R = Wand(screen_height, 0, 119)
    cluster = Cluster()
    zufallsform = Formen.L

    while True:
        stdscr.clear()
        
        boden.draw(stdscr.addstr, '=')
        wand_L.draw(stdscr.addstr, '|\n')

        wand_R.draw_Rechts(stdscr.addstr, '|')

        cluster.waehleForm(Formen(zufallsform))
        cluster.setForm()
        cluster.drawCluster(stdscr)

        for c in unbewegbare_clusters:
            c.drawCluster(stdscr)
        
        bewegbarer_cluster = cluster # Jeder neu erzeugte Cluster, der dem Variable 'bewegbarer_cluster' zugewiesen bekommt, darf nur durch diese Zuweisung bewegt werden

        key = stdscr.getch()
        if key == ord('q'):
            break
        if key == curses.KEY_UP and y > 0:
            y -= 1

        if boden.check_ifCollide_Boden(cluster.get_Seite('U')) == False:
            if key == curses.KEY_DOWN: y += 1
        else: # Cluster haftet am Boden und kann nicht mehr bewegt werden, der Cluster wird von diesem Variable entfernt 
            bewegbarer_cluster = None
            unbewegbare_clusters.append(cluster)
            zufallsform = random.randint(1,5)
            x, y = 50, 0 # draw Koordinaten
            cluster = Cluster()
            bewegbarer_cluster = cluster

        if wand_R.check_ifCollide_Wand(cluster.get_Seite('R')) == False:
            if key == curses.KEY_RIGHT: x += 1

        if wand_L.check_ifCollide_Wand(cluster.get_Seite('L')) == False:
            if key == curses.KEY_LEFT: x -= 1

        if bewegbarer_cluster != None:
            bewegbarer_cluster.setPos(y,x)
        
curses.wrapper(main)