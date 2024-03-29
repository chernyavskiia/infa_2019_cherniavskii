from graph import *
c=canvas()
windowSize(700,700)
penColor("black")
brushColor("grey")
rectangle(0,0,2000,300)
penColor('grey')
brushColor("white")
circle(120,340,90)
penColor('white')
brushColor('white')
rectangle(15,340,230,450)
penColor('grey')
line(31,317,207,317) #niz
line(40,287,205,287) #verch
line(71,317,71,340)
line(115,317,115,340)
line(159,317,159,340)
line(47,287,47,317)
line(84,287,84,317)
line(123,287,123,317)
line(165,287,165,317)
line(55,287,55,110)
line(81,287,81,110)
line(110,287,110,110)
line(138,287,138,110)
line(160,287,160,110)
line(28,340,212,340)
penColor('white')
c.create_oval(290,325,390,475, outline='#696969',fill='#696969',width=1)#tulovische
rectangle(290,415,390,515)
penColor('#2F4F4F')
brushColor('#2F4F4F')
rectangle(330,340,350,425)
c.create_oval(300,450,335,470, outline='#696969',fill='#696969',width=1)#stopy
c.create_oval(345,450,380,470, outline='#696969',fill='#696969',width=1)
c.create_oval(315,410,335,465, outline='#696969',fill='#696969',width=1)#nogi
c.create_oval(345,410,365,465, outline='#696969',fill='#696969',width=1)
rectangle(290,415,390,425)
brushColor('#C0C0C0')
circle(340,320,40)
brushColor('#696969')
circle(340,320,30)
brushColor('#DCDCDC')
circle(340,322,25)#golova
line(327,313,338,320)#glaza
line(353,313,342,320)
polyline([(329,331),(333,328),(337,327),(341,327),(345,328),(349,331)])#rot
c.create_oval(253,355,320,370, outline='#696969',fill='#696969',width=1)#ruka
c.create_oval(360,355,430,370, outline='#696969',fill='#696969',width=1)
line(256,285,256,460)
c.create_oval(70,400,140,425, outline='#696969',fill='#696969',width=1)#koshka
brushColor('#696969')
circle(69,400,15)
polygon([(71,387),(73,381),(77,389)])
polygon([(61,389),(63,381),(65,387)])
brushColor('white')
circle(64,396,4)
circle(74,396,4)
brushColor('black')
circle(66,396,2)
circle(76,396,2)
c.create_oval(77,413,85,447, outline='#696969',fill='#696969',width=1)#lapka
c.create_oval(91,413,100,447, outline='#696969',fill='#696969',width=1)
c.create_oval(116,413,125,447, outline='#696969',fill='#696969',width=1)
c.create_oval(128,413,137,447, outline='#696969',fill='#696969',width=1)
c.create_oval(130,375,140,425, outline='#696969',fill='#696969',width=1)#khvost
run()