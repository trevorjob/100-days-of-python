from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4) 
        nr_numbers = random.randint(2, 4)
        password_list = []
        password_list.extend([random.choice(letters) for _ in range(nr_letters)])
        password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
        password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

        random.shuffle(password_list)
        password = "".join(password_list)
        password_entry.insert(0,password )
        pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
        em = email_entry.get()
        ps = password_entry.get()
        wb = web_entry.get()
        new_data = {
                wb:{
                        "email": em,
                        "password":ps,
                }
                }
        if len(wb) == 0 or len(ps) == 0:
                messagebox.askokcancel(title="message fields",message="please fill in all the fields")
                return
                
        check = messagebox.askokcancel(title=wb, message=f"these are your info : email: {em}, website: {wb}, password: {ps}")
        if check:
                try:
                        with open(file= "data.json" , mode="r") as fie:
                                # write
                                # json.dump(new_data,fie, indent=4)
                                # read
                                data = json.load(fie)
                                data.update(new_data)
                except:
                        with open(file= "data.json" , mode="w") as fie:
                                json.dump(new_data,fie, indent=4)
                else:
                        with open(file= "data.json" , mode="w") as fie:
                                json.dump(data,fie, indent=4)
                finally:        
                        password_entry.delete(0,END)
                        web_entry.delete(0,END)

def search():
        wb = web_entry.get()
        try:
                with open(file= "data.json" , mode="r") as fie:
                        data = json.load(fie)
        except FileNotFoundError:
                messagebox.askokcancel(title=f"{wb}",message=f"there is no data file")
        except:
                messagebox.askokcancel(title=f"{wb}",message=f"there is no info on {wb}")
        else:
                messagebox.askokcancel(title=f"{wb}",message=f"here is the email:{data[wb]['email']} and password: {data[wb]['password']}")
                
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("pomodoro")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file='./logo.png')
canvas.create_image(100,100, image=photo)
canvas.grid(column=1, row=0)

website = Label(text="Website")
website.grid(column=0, row=1)
email = Label(text="Email/Username")
email.grid(column=0, row=2)
password = Label(text="Password")
password.grid(column=0, row=3)


web_entry = Entry(width=21,)
web_entry.grid(column=1, row=1)
web_entry.focus()


email_entry = Entry(width=35)
email_entry.insert(0, "Redeks123456@gmail.com")
email_entry.grid(column=1, row=2,columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

pass_gen = Button(text="generate Password", command=generate_password)
pass_gen.grid(column=2, row=3)


button = Button(text="Add", width=30, command=save)
button.grid(column=1, row=4, columnspan=2)

search_btn = Button(text="Search", width=14,command=search)
search_btn.grid(column=2, row=1)

window.mainloop()