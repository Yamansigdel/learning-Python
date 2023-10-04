from turtle import *
speed(0)
colormode(255)
def moveto(x,y):
    up()
    goto(x,y)
    down()
color('white')
bgcolor("black")
pensize(2)

#for center
x=0
while x<30:
    circle(50)
    rt(15)
    x=x+1
moveto(0,0)
rt(90)

#for 1st quadrant

moveto(250,250)
lt(90)
color('white')
x=0
while x<30:
    circle(50)
    rt(15)
    x=x+1
moveto(250,250)
y=0
color('black')
while y<30:
    circle(75)
    rt(15)
    y=y+1

#for 2nd quadrant

moveto(-250,250)
lt(90)
color('white')
x=0
while x<30:
    circle(50)
    rt(15)
    x=x+1
moveto(-250,250)
y=0
color('black')
while y<30:
    circle(75)
    rt(15)
    y=y+1

#for 3rd quadrant
    
moveto(-250,-250)
lt(90)
color('white')
x=0
while x<30:
    circle(50)
    rt(15)
    x=x+1
moveto(-250,-250)
y=0
color('black')
while y<30:
    circle(75)
    rt(15)
    y=y+1

#for 4rth quadrant

moveto(250,-250)
lt(90)
color('white')
x=0
while x<30:
    circle(50)
    rt(15)
    x=x+1

y=0
color('black')
while y<30:
    circle(75)
    rt(15)
    y=y+1
color('white')
pensize(8)

rt(90)
for i in range(3):
    fd(500)
    lt(90)
    
fd(500)
pensize(4)
color('black')

for i in range(4):
    lt(90)
    fd(500)






