from turtle import *
from random import randint 
speed(0)
colormode(255)
bgcolor("black")
lt(90)
fd(100)
rt(90)

x=0
while x<400:
    r=randint(0,255)
    g=randint(0,255)
    b=randint(0,255)

    pencolor(r,g,b)

    fd(50+x)
    rt(91.11)
    
    x=x+1
    

