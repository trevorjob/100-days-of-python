from tkinter import *


window = Tk()
window.title("mile to km converter")
window.config(padx=20,pady=20)

# ENTRY: I/O
input = Entry(width=10)
input.grid(column=1,row=0)



lab1 = Label(text="is equal to", font=("arial",24,"italic"))
lab1.config(padx=10,pady=10)
lab1.grid(column=0, row=1)

lab3 = Label(text="miles", font=("arial",24,"italic"))
lab3.config(padx=10,pady=10)
lab3.grid(column=2, row=0)

lab2 = Label(text="0", font=("arial",24,"italic"))
lab2.config(padx=10,pady=10)
lab2.grid(column=1, row=1)

lab4 = Label(text="km", font=("arial",24,"italic"))
lab4.config(padx=10,pady=10)
lab4.grid(column=2, row=1)

def button_clicked():
        num = round(float(input.get()) * 1.609)
        lab2.config(text=num)
# BUTTONS
button = Button(text="click me", command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()