from turtle import *
speed(1)
def moveto(x,y):
    up()
    goto(x,y)
    down()
def move(x,y):
    goto(x,y)
for i in range(4):
    fd(100)
    rt(90)
moveto(50,50)
back(100)
for i in range(4):
    fd(100)
    rt(90)
move(0,0)
moveto(50,50)
move(100,0)
moveto(-50,-50)
move(0,-100)
moveto(50,-50)
move(100,-100)

