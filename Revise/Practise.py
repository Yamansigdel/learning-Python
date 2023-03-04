from tkinter import *
main=Tk()

def leftkey(event):
    print('Left Key pressed')

def Rightkey(event):
    print('Right Key pressed')

main.bind('<Left>',leftkey)
main.bind('<Right>',Rightkey)

main.mainloop()

