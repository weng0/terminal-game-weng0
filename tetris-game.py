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

class TetrisGame:
    def __init__(self):
        self.x_start = 37 # Startpunkt
        self.y_start = 0 # Startpunkt
        self.screen_width = 80 # screen_width (max 120) original: 119
        self.screen_height = 30 # screen_height (max 30)
        self.boden = Boden(self.screen_width, self.screen_height, 0)
        self.wand_L = Wand(self.screen_height, 0, 0)
        self.wand_R = Wand(self.screen_height, 0, self.screen_width) # 119
        self.feste_clusters = ClusterFest()
        self.cluster = Cluster(self.y_start, self.x_start)
        self.zufallsform = Formen.T

    def main(self,stdscr):
        # Bildschirm
        stdscr.clear()
        # screen_height, screen_width = stdscr.getmaxyx() // not used
        y, x = self.y_start, self.x_start
        while True:
            stdscr.clear()
            
            self.boden.draw(stdscr.addstr, '=')
            self.wand_L.draw(stdscr.addstr, '|\n')
            self.wand_R.draw_Rechts(stdscr.addstr, '|')

            self.cluster.waehleForm(Formen(self.zufallsform))
            self.cluster.setForm()
            self.cluster.drawCluster(stdscr)
            # stdscr.addstr(0, 40, 'X')

            self.feste_clusters.draw(stdscr)
            
            # Jeder neu erzeugte Cluster, der dem Variable 'bewegbarer_cluster' zugewiesen bekommt, darf nur durch diese Zuweisung bewegt werden

            isBoden = self.boden.check_ifCollide_Boden(self.cluster.get_Seite('U'))
            isFCluster = self.feste_clusters.kollidiert_oben(self.cluster.get_Seite('U'))
            isFCluster_R = self.feste_clusters.kollidiert_seitlich(self.cluster.get_Seite('L'), 'R')  # Wenn Cluster_R -> Fest_L / Fest_R <- Cluster_L
            isFCluster_L = self.feste_clusters.kollidiert_seitlich(self.cluster.get_Seite('R'), 'L')
            kollidiert = False
            # Wenn keine Tasten gedrückt werden, dann werden sämtliche Funktionen, die nach key = stdscr.getch() kommen, gar nicht ausgeführt
            key = stdscr.getch()
            if key == ord('q'):
                break

            if key == curses.KEY_UP and y > 0:
                y -= 1
                self.cluster.setPos(y,x)
            if key == curses.KEY_DOWN:
                if isBoden == False and isFCluster == False: # and isFCluster_L == False
                    y += 2
                    self.cluster.setPos(y,x)
                else: # Cluster haftet am Boden und kann nicht mehr bewegt werden, der Cluster wird von diesem Variable entfernt 
                    kollidiert = True
            
            if self.wand_R.check_ifCollide_Wand(self.cluster.get_Seite('R')) == False:
                if key == curses.KEY_RIGHT:
                    if isFCluster_L == False:
                        x += 3
                        self.cluster.setPos(y,x)

            if self.wand_L.check_ifCollide_Wand(self.cluster.get_Seite('L')) == False:
                if key == curses.KEY_LEFT:
                    if isFCluster_R == False:
                        x -= 3
                        self.cluster.setPos(y,x)

            if kollidiert == True:
                self.feste_clusters.unbewegbare_clusters.append(self.cluster) # !!!
                self.zufallsform = random.randint(1,5)
                y, x = self.y_start, self.x_start # draw Koordinaten
                self.cluster = Cluster(y, x)

game = TetrisGame()
curses.wrapper(game.main)