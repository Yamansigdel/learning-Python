from turtle import *
screen=getscreen()
screen.setworldcoordinates(0,-1000,1000,0)
dr=Turtle()
delay(0)
speed(0)


#FOR PEN
color('black')
def moveto(x,y):
            up()
            goto(x,y)
            down()
moveto(100,-400)
shape('circle')
pensize(8)
ondrag(moveto)
tracer(1)

#FOR COLOR BOX

#1
dr.begin_fill()
dr.fillcolor('red')
for i in range(4):
    dr.fd(100)
    dr.rt(90)
dr.end_fill()
dr.fd(100)    

#2
dr.begin_fill()
dr.fillcolor('orange')
for i in range(4):
    dr.fd(100)
    dr.rt(90)
dr.end_fill()
dr.fd(100)   
#3
dr.begin_fill()
dr.fillcolor('blue')
for i in range(4):
    dr.fd(100)
    dr.rt(90)
dr.end_fill()
dr.fd(100)   
#4
dr.begin_fill()
dr.fillcolor('green')
for i in range(4):
    dr.fd(100)
    dr.rt(90)
dr.end_fill()
dr.fd(100)   
#5
dr.begin_fill()
dr.fillcolor('yellow')
for i in range(4):
    dr.fd(100)
    dr.rt(90)
dr.end_fill()
dr.fd(100)
dr.bk(500)
dr.rt(90)
dr.fd(100)
dr.lt(90)
#6
dr.begin_fill()
dr.fillcolor('violet')
for i in range(4):
    dr.fd(100)
    dr.rt(90)
dr.end_fill()
dr.fd(100)   
#7
dr.begin_fill()
dr.fillcolor('indigo')
for i in range(4):
    dr.fd(100)
    dr.rt(90)
dr.end_fill()
dr.fd(100)   
#8
dr.begin_fill()
dr.fillcolor('Grey')
for i in range(4):
    dr.fd(100)
    dr.rt(90)
dr.end_fill()
dr.fd(100)   
#9
dr.begin_fill()
dr.fillcolor('Brown')
for i in range(4):
    dr.fd(100)
    dr.rt(90)
dr.end_fill()
dr.fd(100)   
#10
dr.begin_fill()
dr.fillcolor('White')
for i in range(4):
    dr.fd(100)
    dr.rt(90)
dr.end_fill()
dr.fd(100)

dr.hideturtle()

def action(x,y):
    if x>=0 and x<100 and y<=0 and y>-100:
         color("red")
    elif x>=100 and x<200 and y<=0 and y>-100:
        color("orange")
    elif x>=200 and x<300 and y<=0 and y>-100:
        color("blue")
    elif x>=300 and x<400 and y<=0 and y>-100:
        color("green")
    elif x>=400 and x<=500 and y<=0 and y>-100:
        color("yellow")
    elif  x>=0 and x<100 and y<=-100 and y>=-200:
        color("violet")
    elif x>=100 and x<200 and y<=-100 and y>=-200:
        color("indigo")
    elif x>=200 and x<300 and y<=-100 and y>=-200:
        color("grey")
    elif x>=300 and x<400 and y<=-100 and y>=-200:
        color("brown")
    elif x>=400 and x<=500 and y<=-100 and y>=-200:
       color("White")
        

screen.onclick(action)

#UPTO HERE





