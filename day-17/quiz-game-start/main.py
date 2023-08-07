from question_model import Question
from data import question_data
from quiz_brain import QuizBrain



question_bank = []
for i in question_data:
        new_q = Question(i["question"], i["correct_answer"])
        question_bank.append(new_q)
        

quiz_brain = QuizBrain(question_bank)

quiz_brain.start_quiz()

print(f"quiz ended you got {quiz_brain.score} out of {quiz_brain.question_number}")