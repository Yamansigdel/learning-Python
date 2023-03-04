from tkinter import *
root=Tk()
root.geometry("350x350+500+250")
root.resizable(0,0)
root.title("PUZZLE")



#commands
def click(b):
    selected.append(b)
    if len(selected) == 2:
        # get grid information of the selected buttons
        info1 = selected[0].grid_info()
        info2 = selected[1].grid_info()
        # swap the buttons
        selected[0].grid(row=info2['row'], column=info2['column'])
        selected[1].grid(row=info1['row'], column=info1['column'])
        # clear selection
        selected.clear()

selected = []

#Buttons
x=0
y=0
for i in range(9):  
    btn = Button(root,text=i+1, width=15,height=7,relief=RAISED)
    btn.config(command=lambda b=btn: click(b))
    btn.grid(row=x, column=y)
    y=y+1
    if(y==3):
        x=x+1
        y=0
    if(i==8):
        btn["text"]=' '

       
    

    




root.mainloop()
