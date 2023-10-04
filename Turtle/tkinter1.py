from tkinter import *

top=Tk()

C=Canvas(top, bg='red', cursor='circle')
coord=10, 50, 240, 210
arc=C.create_arc(coord, start=0, extent=90, fill="blue")


C.pack()

top.mainloop()
