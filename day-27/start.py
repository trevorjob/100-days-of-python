from tkinter import *

window = Tk()

window.minsize(width=500, height=500)
window.title("my first GUI program")
window.config(padx=20,pady=20)

my_label = Label(text="i am a label", font=("arial",24,"italic"))
my_label["text"] = "testis"
my_label.config(text="new text")
# my_label.place(x=100, y=200,)
# my_label.pack()
my_label.config(padx=10,pady=10)
my_label.grid(column=0, row=0)




def button_clicked():
        my_label.config(text=input.get())
# BUTTONS
button = Button(text="click me", command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

# BUTTONS
button2 = Button(text="click me 2", command=button_clicked)
# button.pack()
button2.grid(column=2,row=0)


# ENTRY: I/O
input = Entry(width=10)
input.grid(column=3,row=2)
# input.pack()
window.mainloop()