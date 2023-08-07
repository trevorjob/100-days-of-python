from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .05
SHORT_BREAK_MIN = .05
LONG_BREAK_MIN = .05
reps = 1
keep = ["👍"]
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
        global keep, reps
        window.after_cancel(timer)
        display.config(text="Timer",fg=GREEN)
        keep.clear()
        display_check.config(text=''.join(keep))
        canvas.itemconfig(timer_text, text="00:00")
        
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
        global reps
        if reps % 2 != 0:
                display.config(text="Work",fg=GREEN)
                count_down(WORK_MIN * 60)
        elif reps % 8 == 0:
                display.config(text="Break",fg=RED)
                count_down(LONG_BREAK_MIN * 60)
                keep.clear()
                
        else:
                display.config(text="Break", fg=PINK)
                count_down(SHORT_BREAK_MIN * 60)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
        count_min = math.floor(count / 60)
        count_sec = count % 60
        
        if count_sec <= 9:
                count_sec = f"0{count_sec}"
        if count_min <= 9:
                count_min = f"0{count_min}"
                
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        if count >= 0:
                global timer
                timer = window.after(1000, count_down, count - 1)
        elif count < 0:
                start_timer()
                if reps % 2 == 0:
                        display_check.config(text=''.join(keep))
                        keep.append("👍")

                

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


display = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"), bg=YELLOW)
display.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file='./tomato.png')
canvas.create_image(101,112, image=photo)
timer_text = canvas.create_text(102,132, text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", command=start_timer)
reset = Button(text="reset", command=reset_timer)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)

display_check = Label(fg=GREEN,font=(FONT_NAME,15,"bold"), bg=YELLOW)
display_check.grid(column=1, row=3)

window.mainloop()