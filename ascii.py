import os, time

class Screen:
    def __init__(self, x, y, char):
        self.x = y
        self.y = x
        self.display = []
        self.char = char
        self.fill(char)
    
    def fill(self, char = None):
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

    def update(self):
        os.system("cls")
        for row in self.display:
            line = ""
            for j in row:
                line += j
            print(line)
    
    def tick(self, fps):
        ms = 1 / fps
        time.sleep(ms)

    
    

