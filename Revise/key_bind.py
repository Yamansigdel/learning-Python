from tkinter import *
main=Tk()

def leftkey(event):
    print('Left Key pressed')

def Rightkey(event):
    print('Right Key pressed')

def Upkey(event):
    print('Up Key pressed')

def Downkey(event):
    print('Down Key pressed')

main.bind('<Left>',leftkey)
main.bind('<Right>',Rightkey)
main.bind('<Up>',Upkey)
main.bind('<Down>',Downkey)

main.mainloop()

