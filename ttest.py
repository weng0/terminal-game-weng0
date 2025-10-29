import os
os.system("echo \033[1;1H")
os.system("echo \033[2J")
import curses
from curses import wrapper
# import curses


# ANSI ESCAPE CODE
def hideCursor(): print('\033[?25l')

def showCursor(): print('\033[?25h')

def moveCursor(h,b): print(f'\033[{h};{b}H')

def moveCursorToOne(): print("\033[1;1H")
def clear(): print('\033[2J')

# getSize() of terminal window size, oben-L:1,1  und unten-R: max size

# main file:

# - direction 
# - position  = x ,y coord

# new game:
class Game: pass
# def __init__(self):
# self.klotz = Klotz()
# pos
# direct
# score
# player data: name, score
# listen for keypress

class Klotz:
    def __init__(self):
        self.direction = None
        self.body = None

    def moveKlotz(self, num):
        space = ''
        for i in range(num):
            space += ' '
        return space

    def makeKlotz(self, space):
        klotz = ''
        moveCursor(1,1)
        #klotz += ' ___\n|   |\n|___|'

        
        print(self.moveKlotz(space),' ___')
        print(self.moveKlotz(space),'|   |')
        print(self.moveKlotz(space),'|___|')
        #moveCursor(5,10)
        #self.moveKlotz(5)
        #moveCursor(1,5)
        print('######')
        print('#    #')

        print('######')



def main(stdscr):
    stdscr.clear()
    screen_height, screen_width = stdscr.getmaxyx()
    x = 118 # screen_width (max 120)
    y = 29 # screen_height (max 30)
    while True:
        #stdscr.clear()
        stdscr.addstr(29, 118, 'X')
        #stdscr.refresh()
        key = stdscr.getch()
        if key == ord('q'):
            break
    # stdscr.addstr(10, 10, "hello")
curses.wrapper(main)

#     stdscr.refresh()
#     stdscr.getch()


# stdscr = curses.initscr()
# curses.noecho()
# curses.cbreak()
# stdscr.keypad(True)

# stdscr.addstr(10, 10, 'Hello')

# stdscr.refresh()
# stdscr.getkey()

# curses.nocbreak()
# stdscr.keypad(False)
# curses.echo()


# klotz = Klotz()
# for i in range(5):
#     space = int(input())
#     clear()
#     klotz.makeKlotz(space)
