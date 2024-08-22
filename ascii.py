import os
import time
from sys import platform


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
        os.system(self.clear_command)
        for row in self.display:
            line = ""
            for j in row:
                line += j
            print(line)

    def tick(self, fps):
        ms = 1 / fps
        time.sleep(ms)
