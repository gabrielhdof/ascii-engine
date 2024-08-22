from ascii import Screen

WIDTH = 40
HEIGHT = 10

screen = Screen(WIDTH, HEIGHT, "-")


x = 0
y = 0

while True:
    screen.fill()
    if x < screen.x:
        if y < screen.y:
            screen.draw("uwu", x, y)
            y += 1
        else:
            x += 1
            y = 0

    screen.update()
    screen.tick(30)
