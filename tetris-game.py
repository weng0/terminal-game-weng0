import os
os.system("echo \033[1;1H")
os.system("echo \033[2J")
import curses
from curses import wrapper

class Game: pass

class Klotz: pass

def main(stdscr):
    stdscr.clear()
    # screen_height, screen_width = stdscr.getmaxyx() // not used
    x = 118 # screen_width (max 120)
    y = 29 # screen_height (max 30)
    while True:
        stdscr.clear()
        stdscr.addstr(y, x, 'X')
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



