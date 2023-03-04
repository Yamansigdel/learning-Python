from turtle import *
from random import *

speed(0)
colormode(255)
bgcolor("black")
hideturtle()
rt(90)
fd(250)
lt(90)
x=0
while x<300:
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)
    pencolor(r,g,b)
    
    circle(x)
    x=x+1
