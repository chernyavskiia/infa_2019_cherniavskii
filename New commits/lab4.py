file = open("file.txt", "a", newline="\n")
from tkinter import *
from random import randrange as rnd, choice
import time
from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=2)
print('YOUR NAME:')
name = str(input())


scores = {}

colors = ['red', 'orange', 'navy', 'purple', 'black', 'yellow', 'green', 'blue']
a = 3


def new():
    global x1, y1, r1, ball1, vx1, vy1, a
    global x2, y2, r2, ball2, vx2, vy2
    x1 = rnd(50, 700)
    y1 = rnd(50, 500)
    r1 = rnd(30, 90)
    ball1 = canv.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill=choice(colors), width=0, tag='ball1')
    vx1 = rnd(-2, 2)
    vy1 = rnd(-2, 2)
    x2 = rnd(50, 700)
    y2 = rnd(50, 500)
    r2 = rnd(30, 90)
    ball2 = canv.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill=choice(colors), width=0, tag='ball2')
    vx2 = rnd(-3, 3)
    vy2 = rnd(-3, 3)
    move()


def move():
    global x1, y1, vx1, vy1
    global x2, y2, vx2, vy2

    canv.move(ball1, vx1, vy1)
    x1 = x1 + vx1
    y1 = y1 + vy1

    canv.move(ball2, vx2, vy2)
    x2 = x2 + vx2
    y2 = y2 + vy2

    root.after(50, move)

    if x1 - r1 < 0 or x1 + r1 > 800:
        vx1 *= -1
    if y1 - r1 < 0 or y1 + r1 > 600:
        vy1 *= -1

    if x2 - r2 < 0 or x2 + r2 > 800:
        vx2 *= -1
    if y2 - r2 < 0 or y2 + r2 > 600:
        vy2 *= -1


schyot = 0


def click(event):
    global x1, y1, r1, ball1, vx1, vy1, a, schyot
    global x2, y2, r2, ball2, vx2, vy2
    if (event.x - x1) ** 2 + (event.y - y1) ** 2 <= r1 ** 2:
        canv.delete('schyot', 'ball1')
        canv.create_text(350, 50, text='score:' + str(schyot + 1), font="times 28", tag='schyot')
        schyot = schyot + 1
        x1 = rnd(50, 700)
        y1 = rnd(50, 500)
        r1 = rnd(30, 90)
        ball1 = canv.create_oval(x1 - r1, y1 - r1, x1 + r1, y1 + r1, fill=choice(colors), width=0, tag='ball1')
        vx1 = rnd(-2, 2)
        vy1 = rnd(-2, 2)
    if (event.x - x2) ** 2 + (event.y - y2) ** 2 <= r1 ** 2:
        canv.delete('schyot', 'ball2')
        canv.create_text(350, 50, text='score:' + str(schyot + 1), font="times 28", tag='schyot')
        x2 = rnd(50, 700)
        y2 = rnd(50, 500)
        r2 = rnd(30, 90)
        ball2 = canv.create_oval(x2 - r2, y2 - r2, x2 + r2, y2 + r2, fill=choice(colors), width=0, tag='ball2')
        vx2 = rnd(-3, 3)
        vy2 = rnd(-3, 3)
        schyot = schyot + 1


new()
canv.bind('<Button-1>', click)
mainloop()
file.write(name +':' + str(schyot)+'\n')

file.close()
