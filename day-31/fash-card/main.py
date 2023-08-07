import pandas
from random import choice
from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


try:
        words_to_learn = pandas.read_csv("./words_to_learn.csv")
except FileNotFoundError:
        data = pandas.read_csv('./data/french_words.csv')
        learn = data.to_dict(orient='records')
else:
        learn = words_to_learn.to_dict(orient='records')
# language = [[val.French, val.English] for idx,val in data.iterrows()]
ran = ""
# print(ran)
def switch_words(button):
        global ran, flip
        window.after_cancel(flip)
        ran = choice(learn)
        make(photo,'French', "black")
        
        if button == "right":
                filename = 'words_to_learn.csv'
                learn.remove(ran)
                new_file = pandas.DataFrame(learn)
                new_file.to_csv(filename, index=False)
        
        window.after(3000, change)


def change():        
        make(photo1,'English', "white")

def make(photo, word, fill):
        new_canvas = canvas.create_image(400,263, image=photo)
        canvas.itemconfig(new_canvas, image=photo)
        card_language = canvas.create_text(400,180,fill=fill, font=('arial',40,"italic"))
        card_word = canvas.create_text(400,263,fill=fill, font=('arial',56,"bold"))

        canvas.itemconfig(card_word,text=f'{ran[word]}')
        canvas.itemconfig(card_language,text=word)

window = Tk()
window.title("flash card")

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip = window.after(3000, change)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
photo = PhotoImage(file='./images/card_front.png')
photo1 = PhotoImage(file='./images/card_back.png')
canvas.create_image(400,263, image=photo)
card_language = canvas.create_text(400,180,fill="black", font=('arial',40,"italic"))
card_word = canvas.create_text(400,263,fill="black", font=('arial',56,"bold"))
canvas.grid(column=0, row=0, columnspan=2)



right_img = PhotoImage(file='./images/right.png',)
right = Button(window,image=right_img)
right.config(command=lambda button=right:switch_words("right"))
right.grid(column=0, row=1)
wrong_img = PhotoImage(file='./images/wrong.png',)
wrong = Button(window, image=wrong_img)
wrong.config(command=lambda button=wrong:switch_words("wrong"))
wrong.grid(column=1, row=1)

switch_words("")
window.mainloop()