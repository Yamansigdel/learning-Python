from tkinter import *

window=Tk()
window.title("My Computer Science Glossary")
window.configure(bg="black")
window.geometry("800x600+350+50")

#Photo
#photo1=PhotoImage(file="file:///C:/Users/Admin/OneDrive/Desktop/shutterstock-392723320.webp")

#Label(window, bg="black").grid(row=0, column=0, sticky=W)

#Space_label
Label(window, bg="black", height=3).grid(row=1, sticky=W)

#Label
Label(window, text="Enter the word:", bg="black", fg="white", font="none 12 bold").grid(row=2, column=0, sticky=W)

#click_command
def click():
    entered_text=textentry.get()
    output.delete(0.0, END)
    try:
        definition= my_dictionary[entered_text]
    except:
        definition="sorry there is no word like that please try again"
    output.insert(END, definition)

#create a text entry box
textentry=Entry(window, width=20, bg="white")
textentry.grid(row=3, column=0, sticky=W)

#add a submit button
Button(window, text="SUBMIT", width=6, command=click, relief="groove").grid(row=4, column=0, sticky=W)


#Space_Label
Label(window, height=3, bg="black").grid(row=5, sticky=W)

#Label_next
Label(window, text="Definition:", bg="black", fg="white", font="none 12 bold").grid(row=6, column=0, sticky=W)

#text_box
output=Text(window, width=65, height=6, wrap=WORD, bg="white")
output.grid(row=7, column=0, sticky=W)

#use dictionary
my_dictionary={
    'algorithm': 'Step by step instruction to complete a task', 'bug': 'piece of code that causes a program to fall'
    }

#exit_command
def close():
    window.destroy()
    exit()    

#exit
Button(window, text="Exit", width=8, command=close, relief="groove").grid(row=8, column=0, sticky=W)


window.mainloop()
