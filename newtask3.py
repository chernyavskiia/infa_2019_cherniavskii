from graph import *
def window(x,y):
    penColor('white')
    brushColor('white')
    rectangle(x,y,x-75,y-190)
    brushColor(164,223,242)
    rectangle(x-5,y-5,x-70,y-183)
    penSize(5)
    line(x,y-120,x-70,y-120)
    line(x-37,y,x-37,y-190)
    penSize(1)
def oval(a,b,x,y):
    list=[]
    if int(a)!=0:
        for i in range(int(-a),int(a),1):
            z=y+b*((1-(i/a)**2)**(0.5))
            list.append((i+x,z))
        for i in range(int(a),int(-a),-1):
            z2 = y - b * ((1 - (i / a) ** 2) ** (0.5))
            list.append((i + x, z2))
        return list
    else:
        penSize(2)
        return [(x,y-b),(x,y+b)]

def ellipse (x,y,x1,y1,a):
    for i in range(min(int(x1),int(x)) - int(a), max(int(x1),int(x)) + int(a), ++1):
        for j in range(min(int(y1),int(y)) - int(a), max(int(y1),int(y)) + int(a), ++1):
            if ((x-i)**2 + (y-j)**2)**0.5 + ((x1-i) ** 2+ (y1-j) **2) **0.5 <= a:
                point(i,j)
    for i in range(min(int(x1),int(x)) - int(a), max(int(x1),int(x)) + int(a), ++1):
        for j in range(min(int(y1),int(y)) - int(a), max(int(y1),int(y)) + int(a), ++1):
            if int(((x-i)**2 + (y-j)**2)**0.5 + ((x1-i) ** 2+ (y1-j) **2) **0.5 )== int(a):
                penColor('black')
                point(i,j)


def klubok(size,lr,x,y):
    brushColor(153,153,153)
    circle(319*size+x,520*size+y, 28*size)
    polyline([(318*size+x,520*size+y),(322*size+x,524*size+y),(326*size+x,531*size+y),(329*size+x,540*size+y),(329*size+x,547*size+y)])
    polyline([(324*size+x,512*size+y),(330*size+x,520*size+y),(335*size+x,530*size+y),(337*size+x,543*size+y)])
    polyline([(310*size+x,528*size+y),(315*size+x,535*size+y),(316*size+x,547*size+y)])
    polyline([(299*size+x,536*size+y),(303*size+x,524*size+y),(307*size+x,516*size+y),(319*size+x,508*size+y),(329*size+x,509*size+y)])
    polyline([(294*size+x,533*size+y),(295*size+x,524*size+y),(300*size+x,516*size+y),(305*size+x,512*size+y),(309*size+x,507*size+y),(319*size+x,502*size+y),(324*size+x,500*size+y)])
def klubokkrasny(size,lr,x,y):
    brushColor(255, 0, 0)
    circle(319*size+x,520*size+y, 28*size)
    polyline([(318*size+x,520*size+y),(322*size+x,524*size+y),(326*size+x,531*size+y),(329*size+x,540*size+y),(329*size+x,547*size+y)])
    polyline([(324*size+x,512*size+y),(330*size+x,520*size+y),(335*size+x,530*size+y),(337*size+x,543*size+y)])
    polyline([(310*size+x,528*size+y),(315*size+x,535*size+y),(316*size+x,547*size+y)])
    polyline([(299*size+x,536*size+y),(303*size+x,524*size+y),(307*size+x,516*size+y),(319*size+x,508*size+y),(329*size+x,509*size+y)])
    polyline([(294*size+x,533*size+y),(295*size+x,524*size+y),(300*size+x,516*size+y),(305*size+x,512*size+y),(309*size+x,507*size+y),(319*size+x,502*size+y),(324*size+x,500*size+y)])
def klubokzholty(size,lr,x,y):
    brushColor(255, 255, 0)
    circle(319*size+x,520*size+y, 28*size)
    polyline([(318*size+x,520*size+y),(322*size+x,524*size+y),(326*size+x,531*size+y),(329*size+x,540*size+y),(329*size+x,547*size+y)])
    polyline([(324*size+x,512*size+y),(330*size+x,520*size+y),(335*size+x,530*size+y),(337*size+x,543*size+y)])
    polyline([(310*size+x,528*size+y),(315*size+x,535*size+y),(316*size+x,547*size+y)])
    polyline([(299*size+x,536*size+y),(303*size+x,524*size+y),(307*size+x,516*size+y),(319*size+x,508*size+y),(329*size+x,509*size+y)])
    polyline([(294*size+x,533*size+y),(295*size+x,524*size+y),(300*size+x,516*size+y),(305*size+x,512*size+y),(309*size+x,507*size+y),(319*size+x,502*size+y),(324*size+x,500*size+y)])
def klubokzelyony(size,lr,x,y):
    brushColor(0, 128, 0)
    circle(319*size+x,520*size+y, 28*size)
    polyline([(318*size+x,520*size+y),(322*size+x,524*size+y),(326*size+x,531*size+y),(329*size+x,540*size+y),(329*size+x,547*size+y)])
    polyline([(324*size+x,512*size+y),(330*size+x,520*size+y),(335*size+x,530*size+y),(337*size+x,543*size+y)])
    polyline([(310*size+x,528*size+y),(315*size+x,535*size+y),(316*size+x,547*size+y)])
    polyline([(299*size+x,536*size+y),(303*size+x,524*size+y),(307*size+x,516*size+y),(319*size+x,508*size+y),(329*size+x,509*size+y)])
    polyline([(294*size+x,533*size+y),(295*size+x,524*size+y),(300*size+x,516*size+y),(305*size+x,512*size+y),(309*size+x,507*size+y),(319*size+x,502*size+y),(324*size+x,500*size+y)])

def kluboksiny(size,lr,x,y):
    brushColor(70, 130, 180)
    circle(319*size+x,520*size+y, 28*size)
    polyline([(318*size+x,520*size+y),(322*size+x,524*size+y),(326*size+x,531*size+y),(329*size+x,540*size+y),(329*size+x,547*size+y)])
    polyline([(324*size+x,512*size+y),(330*size+x,520*size+y),(335*size+x,530*size+y),(337*size+x,543*size+y)])
    polyline([(310*size+x,528*size+y),(315*size+x,535*size+y),(316*size+x,547*size+y)])
    polyline([(299*size+x,536*size+y),(303*size+x,524*size+y),(307*size+x,516*size+y),(319*size+x,508*size+y),(329*size+x,509*size+y)])
    polyline([(294*size+x,533*size+y),(295*size+x,524*size+y),(300*size+x,516*size+y),(305*size+x,512*size+y),(309*size+x,507*size+y),(319*size+x,502*size+y),(324*size+x,500*size+y)])


def kot(x,y,color,lr,size):
    if color==1:
        brushColor(200, 113, 55)
        penColor(200,113,55)
    else:
        brushColor(108,93,83)
        penColor(108,93,83)
    ellipse(x+70*size*lr,y,x+130*size*lr,y+40*size,80*size)#khvost
    penColor('black')
    polygon(oval(size * 80, size * 40, x, y))
    polygon(oval(size*16,size*50,x - 70 * size*lr, y + 19 * size))#perednyayapravaya
    polygon(oval(size*20,size*50,x+60*size*lr,y+45*size))#zadnyaya
    circle(x-75*size*lr,y-5*size,size*32)#golova
    polygon(oval(size*17,size*43,x-45*size*lr,y+48*size))#perednyaya levaya
    brushColor(223,171,135)
    polygon([(x-105*size*lr,y-20*size),(x-105*size*lr,y-40*size),(x-90*size*lr,y-30*size)])
    polygon([(x-60*size*lr,y-30*size),(x-45*size*lr,y-40*size),(x-45*size*lr,y-20*size)])
    polygon([(x-71*size*lr,y+10*size),(x-79*size*lr,y+10*size),(x-75*size*lr,y+14*size)])

    line(x-75*size*lr, y+14*size, x-75*size*lr, y+18*size)
    if color==1:
        brushColor(136, 170, 0)
    else:
        brushColor(42,212,255)
    circle(x-88*size*lr,y-2*size,size*9)
    circle(x-60*size*lr,y-2*size,size*9)
    brushColor('black')
    polygon(oval(size*1,size*9,x-92*size*lr,y-2*size))
    polygon(oval(size*1,size*9,x-64*size*lr,y-2*size))
    penSize(1)

brushColor(125,104,0)
rectangle(0,313,500,700)
brushColor(85,70,0)
rectangle(0,0,500,313)
window(60,230)
window(160,230)
window(260,230)
window(360,230)
window(460,230)
brushColor(190,110,60)
penColor(190,110,60)
penSize(1)
kot(335,373,1,1,1)
kot(85,380,1,-1,0.3)
kot(143,451,-1,-1,1)
kot(170,550,-1,-1,0.3)
kot(360,500,1,1,0.3)
kot(450,450,1,-1,0.3)
kot(450,550,-1,1,0.3)
klubokkrasny(0.5,1,220,200)
klubokzholty(0.5,1,-30,260)
klubokkrasny(0.5,1,-10,120)
klubok(1.5,1,-210,-250)
kluboksiny(1,1,0,-60)
klubokzholty(1,1,120,-25)
klubokzelyony(0.5,1,220,300)

run()