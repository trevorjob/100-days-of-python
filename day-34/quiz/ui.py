from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
class QuizInterface:
        def __init__(self, quizbrain: QuizBrain):
                self.quiz = quizbrain
                self.window = Tk()
                self.window.title("Quizzler")
                self.window.config(padx=20, pady=20, bg=THEME_COLOR)
                self.window.minsize(width=300, height=250)
                
                self.score = Label(text=f"score: {self.quiz.score}", fg="white",font=('arial',10,"bold") , bg=THEME_COLOR)
                self.score.grid(column=1, row=0)
                
                self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
                self.question_text = self.canvas.create_text(150,125,fill="black",width=280, font=("arial",20,"italic"))
                self.canvas.grid(column=0, row=1 , columnspan=2,pady=50)
                
                photo = PhotoImage(file='./images/true.png')
                self.true_btn = Button(image=photo, command=self.true_check)
                self.true_btn.grid(column=0, row=2)
                
                
                photo2 = PhotoImage(file='./images/false.png')
                self.false_btn = Button(image=photo2, command=self.false_check)
                self.false_btn.grid(column=1, row=2)
                
                self.get_next_question()
                self.window.mainloop()
                
        def get_next_question(self):
                self.canvas.config(bg='white')
                if self.quiz.still_has_questions():
                        self.score.config(text=f"score: {self.quiz.score}")
                        Q_t = self.quiz.next_question()
                        self.canvas.itemconfig(self.question_text, text=Q_t)
                else:
                        self.true_btn.config(state="disabled")
                        self.false_btn.config(state="disabled")
                        self.canvas.itemconfig(self.question_text, text=f"game over your score was {self.quiz.score}/10")
        
        def true_check(self):
                is_right = self.quiz.check_answer("True")
                self.checker(is_right)
        def false_check(self):
                
                is_right = self.quiz.check_answer("false")
                self.checker(is_right)
        
        def checker(self, feedback):
                if feedback:
                        self.canvas.config(bg='green')
                else:
                        self.canvas.config(bg='red')
                
                self.window.after(1000,self.get_next_question)
                
                
                

