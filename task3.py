from graph import *


def window(x, y, width, length):
    penColor('white')
    brushColor('white')
    rectangle(x, y, x - 75 * width / 2, y - 190 * length / 2)
    brushColor(164, 223, 242)
    rectangle(x - 5 * width / 2, y - 5 * length / 2, x - 70 * width / 2, y - 183 * length / 2)
    penSize(5)
    line(x, y - 60 * length, x - 35 * width, y - 60 * length)
    line(x - 20 * width, y, x - 20 * length, y - 95 * width)
    penSize(1)


def oval(a, b, x, y):
    list = []
    if int(a) != 0:
        for i in range(int(-a), int(a), 1):
            z = y + b * ((1 - (i / a) ** 2) ** (0.5))
            list.append((i + x, z))
        for i in range(int(a), int(-a), -1):
            z2 = y - b * ((1 - (i / a) ** 2) ** (0.5))
            list.append((i + x, z2))
        return list
    else:
        penSize(2)
        return [(x, y - b), (x, y + b)]


def ellipse(x, y, x1, y1, a):
    for i in range(min(int(x1), int(x)) - int(a), max(int(x1), int(x)) + int(a), ++1):
        for j in range(min(int(y1), int(y)) - int(a), max(int(y1), int(y)) + int(a), ++1):
            if ((x - i) ** 2 + (y - j) ** 2) ** 0.5 + ((x1 - i) ** 2 + (y1 - j) ** 2) ** 0.5 <= a:
                point(i, j)
    for i in range(min(int(x1), int(x)) - int(a), max(int(x1), int(x)) + int(a), ++1):
        for j in range(min(int(y1), int(y)) - int(a), max(int(y1), int(y)) + int(a), ++1):
            if int(((x - i) ** 2 + (y - j) ** 2) ** 0.5 + ((x1 - i) ** 2 + (y1 - j) ** 2) ** 0.5) == int(a):
                penColor('black')
                point(i, j)


def klubok(size, lr, x, y, z, ):
    list = []
    list.append(brushColor(z))
    list.append(circle(319 * size + x, 520 * size + y, 28 * size))
    list.append(polyline(
        [(318 * size + x, 520 * size + y), (322 * size + x, 524 * size + y), (326 * size + x, 531 * size + y),
         (329 * size + x, 540 * size + y), (329 * size + x, 547 * size + y)]))
    list.append(polyline(
        [(324 * size + x, 512 * size + y), (330 * size + x, 520 * size + y), (335 * size + x, 530 * size + y),
         (337 * size + x, 543 * size + y)]))
    list.append(polyline(
        [(310 * size + x, 528 * size + y), (315 * size + x, 535 * size + y), (316 * size + x, 547 * size + y)]))
    list.append(polyline(
        [(299 * size + x, 536 * size + y), (303 * size + x, 524 * size + y), (307 * size + x, 516 * size + y),
         (319 * size + x, 508 * size + y), (329 * size + x, 509 * size + y)]))
    list.append(polyline(
        [(294 * size + x, 533 * size + y), (295 * size + x, 524 * size + y), (300 * size + x, 516 * size + y),
         (305 * size + x, 512 * size + y), (309 * size + x, 507 * size + y), (319 * size + x, 502 * size + y),
         (324 * size + x, 500 * size + y)]))
    return list


def kot(x, y, color, lr, l, size):
    if l == 1:
        if color == 1:
            brushColor(200, 113, 55)
            penColor(200, 113, 55)
        else:
            brushColor(108, 93, 83)
            penColor(108, 93, 83)
        ellipse(x + 70 * size * lr, y, x + 130 * size * lr, y + 40 * size, 80 * size)  # khvost
        penColor('black')
        polygon(oval(size * 80, size * 40, x, y))
        polygon(oval(size * 18, size * 41, x + 60 * size * lr, y + 45 * size))  # zadnyaya
        polygon(oval(size * 19, size * 8, x + 50 * size * lr, y + 80 * size))
        circle(x - 75 * size * lr, y - 5 * size, size * 32)  # golova
        polygon(oval(size * 17, size * 41, x - 42 * size * lr, y + 46 * size))  # perednyaya levaya
        polygon(oval(size * 19, size * 8, x - 54 * size * lr, y + 80 * size))
        brushColor(223, 171, 135)
        polygon([(x - 105 * size * lr, y - 20 * size), (x - 105 * size * lr, y - 40 * size),
                 (x - 90 * size * lr, y - 30 * size)])
        polygon([(x - 60 * size * lr, y - 30 * size), (x - 45 * size * lr, y - 40 * size),
                 (x - 45 * size * lr, y - 20 * size)])
        polygon([(x - 71 * size * lr, y + 10 * size), (x - 79 * size * lr, y + 10 * size),
                 (x - 75 * size * lr, y + 14 * size)])

        line(x - 75 * size * lr, y + 14 * size, x - 75 * size * lr, y + 18 * size)
        if color == 1:
            brushColor(136, 170, 0)
        else:
            brushColor(42, 212, 255)
        circle(x - 88 * size * lr, y - 2 * size, size * 9)
        circle(x - 60 * size * lr, y - 2 * size, size * 9)
        brushColor('black')
        polygon(oval(size * 1, size * 9, x - 92 * size * lr, y - 2 * size))
        polygon(oval(size * 1, size * 9, x - 64 * size * lr, y - 2 * size))
        penSize(1)
    else:
        if color == 1:
            brushColor(200, 113, 55)
            penColor(200, 113, 55)
        else:
            brushColor(108, 93, 83)
            penColor(108, 93, 83)
        ellipse(x + 70 * size * lr, y, x + 130 * size * lr, y + 40 * size, 80 * size)
        penColor('black')
        polygon(oval(size * 80, size * 40, x, y))
        polygon(oval(size * 12, size * 24, x - 88 * size * lr, y + 12 * size))
        circle(x + 55 * size * lr, y + 20 * size, size * 20)
        polygon(oval(size * 10, size * 20, x + 70 * size * lr, y + 45 * size))
        circle(x - 75 * size * lr, y - 5 * size, size * 32)
        polygon(oval(size * 23, size * 13, x - 55 * size * lr, y + 37 * size))
        brushColor(223, 171, 135)
        polygon([(x - 105 * size * lr, y - 20 * size), (x - 105 * size * lr, y - 40 * size),
                 (x - 90 * size * lr, y - 30 * size)])
        polygon([(x - 60 * size * lr, y - 30 * size), (x - 45 * size * lr, y - 40 * size),
                 (x - 45 * size * lr, y - 20 * size)])
        polygon([(x - 71 * size * lr, y + 10 * size), (x - 79 * size * lr, y + 10 * size),
                 (x - 75 * size * lr, y + 14 * size)])

        line(x - 75 * size * lr, y + 14 * size, x - 75 * size * lr, y + 18 * size)
        if color == 1:
            brushColor(136, 170, 0)
        else:
            brushColor(42, 212, 255)
        circle(x - 88 * size * lr, y - 2 * size, size * 9)
        circle(x - 60 * size * lr, y - 2 * size, size * 9)
        brushColor('black')
        polygon(oval(size * 1, size * 9, x - 85 * size * lr, y - 2 * size))
        polygon(oval(size * 1, size * 9, x - 57 * size * lr, y - 2 * size))
        penSize(1)


brushColor(125, 104, 0)
rectangle(0, 313, 500, 700)
brushColor(85, 70, 0)
rectangle(0, 0, 500, 313)
window(60, 230, 2, 2)
window(160, 230, 1, 1)
window(260, 230, 2, 2)
window(360, 230, 2, 2)
window(460, 230, 2, 2)
brushColor(190, 110, 60)
penColor(190, 110, 60)
penSize(1)
kot(335, 373, 1, 1, 0, 1)
kot(85, 380, 1, -1, 1, 0.3)
kot(143, 451, -1, -1, 1, 1)
kot(170, 550, -1, -1, 1, 0.3)
kot(360, 500, 1, 1, 1, 0.3)
kot(450, 450, 1, -1, 1, 0.3)
kot(450, 550, -1, 1, 1, 0.3)
A = ['Green', 'Yellow', 'Orange', 'Blue', 'Brown']
z = 'black'
s = klubok(0.5, 1, 220, 200, z)
x = -10
y = -10
d_x = 5
d_y = 5
i=0

print(y)
def moving():
    global x
    global y
    global d_x
    global d_y
    global i
    for i in s:
        moveObjectBy(i, d_x, d_y)
    if x > 100 and d_x > 0:
        d_x = (-1) * d_x
        print(x)
    if x < -450 and d_x < 0:
        d_x *= -1
    if y > 200 and d_y > 0:
        d_y = (-1)*d_y
        print(x)
    if y < -430 and d_y < 0:
        d_y *= -1
    x += d_x
    y += d_y
j=0
def changecolor():
    global j
    global z
    global A
    global s
    if j==5:
        j=0
    else:
        s = klubok(0.5, 1, 220, 200, A[j])
    j+=1



onTimer(moving,100)

run()
