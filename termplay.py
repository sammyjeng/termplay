#!/usr/bin/env python3
import curses
import os
import sys

class FileMan:
    """Draw a curses filemanger to display the playlist"""

    def __init__(self, fm):

        self.fm = fm
        curses.wrapper(self.mainloop)


    def mainloop(self, stdscr):
        """Catch the input the keys."""

        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        self.stdscr = stdscr
        self.screen_height, self.screen_width = self.stdscr.getmaxyx()
        current_file = 0
        self.print_fm(current_file)

        while True:

            key_press = self.stdscr.getch()
            if key_press == curses.KEY_UP and current_file > 0:
                current_file -= 1

            elif key_press == curses.KEY_DOWN and current_file < len(self.fm) - 1:
                current_file += 1

            elif key_press == curses.KEY_ENTER or key_press in [10, 13]:
                self.mpv_play(current_file)

            elif key_press == curses.KEY_DOWN and current_file == len(self.fm) -1:
                current_file = 0

            elif key_press == curses.KEY_UP and current_file == 0:
                current_file = len(self.fm) - 1

            elif key_press == curses.KEY_BACKSPACE or key_press == ord('Q'):
                os.system('pkill mpv')
                break

            else:
                current_file = current_file
            self.print_fm(current_file)


    def print_fm(self, current_file_index):
        self.stdscr.clear()
        for index, cfile in enumerate(self.fm):
            x = 1
            y = index + x
            if index == current_file_index:
                self.highlight(y, x, cfile, 1)
            else:
                self.stdscr.addstr(y, x, cfile)
        self.stdscr.refresh()


    def highlight(self, y, x, text, pair_num):
        self.stdscr.attron(curses.color_pair(pair_num))
        self.stdscr.addstr(y, x, text)
        self.stdscr.attroff(curses.color_pair(pair_num))


    def allign(self, text):
        self.stdscr.clear()
        x = 0
        y = 1
        self.stdscr.addstr(y, x, text)
        self.stdscr.refresh()


    def mpv_play(self,current_file, *arg):
        self.stdscr.refresh()
        #os.system("mpv --input-conf=input.conf --loop-playlist -video=no --playlist=list.pl --playlist-start={} 1&2>/dev/null ".format(current_file))
        os.system("mpv --input-conf=input.conf -video=no {}{} 1&2>/dev/null ".format(" ",self.fm[current_file]))
        self.stdscr.clear()



if __name__ == '__main__':
    try:
        item_musik = []
        with open('list.pl','r') as r:
            files = r.readlines(2000)
            for line in files:
                item_musik.append(line)
        fm = item_musik
        FileMan(fm)
    except curses.error as _e:
        print(_e, "check the TODO list https://github.com/sammyjeng/termplay#todo")
