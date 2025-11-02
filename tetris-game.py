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
from src.cluster_fest import ClusterFest
import random
random.seed()
stdscr = curses.initscr()

class TetrisGame: pass

def main(stdscr):
    # Bildschirm
    stdscr.clear()
    # screen_height, screen_width = stdscr.getmaxyx() // not used
    x = 39 # Startpunkt
    y = 0 # Startpunkt
    screen_width = 80 # screen_width (max 120) original: 119
    screen_height = 30 # screen_height (max 30)
    
    feste_clusters = ClusterFest() # unbewegbare_clusters : Cluster = []
    boden = Boden(screen_width, screen_height, 0)
    wand_L = Wand(screen_height, 0, 0)
    wand_R = Wand(screen_height, 0, screen_width) # 119
    cluster = Cluster(y, x)
    zufallsform = Formen.T

    while True:
        stdscr.clear()
        
        boden.draw(stdscr.addstr, '=')
        wand_L.draw(stdscr.addstr, '|\n')
        wand_R.draw_Rechts(stdscr.addstr, '|')

        cluster.waehleForm(Formen(zufallsform))
        cluster.setForm()
        cluster.drawCluster(stdscr)

        feste_clusters.draw(stdscr)
        
        # Jeder neu erzeugte Cluster, der dem Variable 'bewegbarer_cluster' zugewiesen bekommt, darf nur durch diese Zuweisung bewegt werden

        isBoden = boden.check_ifCollide_Boden(cluster.get_Seite('U'))
        isFCluster = feste_clusters.kollidiert_oben(cluster.get_Seite('U'))
        isFCluster_R = feste_clusters.kollidiert_seitlich(cluster.get_Seite('L'), 'R')  # Wenn Cluster_R -> Fest_L / Fest_R <- Cluster_L
        isFCluster_L = feste_clusters.kollidiert_seitlich(cluster.get_Seite('R'), 'L')
        kollidiert = False
        # Wenn keine Tasten gedrückt werden, dann werden sämtliche Funktionen, die nach key = stdscr.getch() kommen, gar nicht ausgeführt
        key = stdscr.getch()
        if key == ord('q'):
            break

        if key == curses.KEY_UP and y > 0:
            y -= 1
            cluster.setPos(y,x)
        if key == curses.KEY_DOWN:
            if isBoden == False and isFCluster == False: # and isFCluster_L == False
                y += 2
                cluster.setPos(y,x)
            else: # Cluster haftet am Boden und kann nicht mehr bewegt werden, der Cluster wird von diesem Variable entfernt 
                kollidiert = True
        
        if wand_R.check_ifCollide_Wand(cluster.get_Seite('R')) == False:
            if key == curses.KEY_RIGHT:
                if isFCluster_L == False:
                    x += 3
                    cluster.setPos(y,x)

        if wand_L.check_ifCollide_Wand(cluster.get_Seite('L')) == False:
            if key == curses.KEY_LEFT:
                if isFCluster_R == False:
                    x -= 3
                    cluster.setPos(y,x)

        if kollidiert == True:
            feste_clusters.unbewegbare_clusters.append(cluster) # !!!
            zufallsform = random.randint(1,5)
            x, y = 50, 0 # draw Koordinaten
            cluster = Cluster(y,x)

curses.wrapper(main)