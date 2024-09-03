import os
import time
from sys import platform
import sys


class Screen:
    def __init__(self, x, y, char):
        self.x = y
        self.y = x
        self.display = []
        self.char = char
        self.fill(char)
        if platform == 'win32':
            self.clear_command = "cls"
        else:
            self.clear_command = "clear"
        os.system(self.clear_command)

    def fill(self, char=None):
        if char is None:
            char = self.char

        self.display = []
        for i in range(self.x):
            row = []
            for j in range(self.y):
                row.append(char)
            self.display.append(row)

    def draw(self, char, x, y):
        self.display[x][y] = char
        for i in range(len(char)):
            if (y + i) >= len(self.display[x]):
                break
            self.display[x][y+i] = char[i]

    def update(self):

        # Move cursor up by the number of lines in display
        # testar [F
        sys.stdout.write("\033[A" * (len(self.display)))

        for row in self.display:
            line = "".join(row)
            # Overwrite the line and clear the rest
            sys.stdout.write("\r" + line + "\033[K\n")

        sys.stdout.flush()

    def tick(self, fps):
        ms = 1 / fps
        time.sleep(ms)
