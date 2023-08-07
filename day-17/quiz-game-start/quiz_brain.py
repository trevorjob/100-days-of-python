class QuizBrain:
        def __init__(self, list) -> None:
                self.list = list
                self.question_number = 0
                self.score =  0
        
        
        def nextQuestion(self):
                question = self.list[self.question_number].text
                self.question_number += 1
                answer = input( f"Q. {self.question_number}: {question} (true/false): ")
                return answer
        
        
        def checkIfCorrect(self):
                player_answer = self.nextQuestion().capitalize()
                actualAnswer = self.list[self.question_number - 1].answer
                if player_answer == actualAnswer:
                        self.score += 1
                        print("you got it right")
                else:
                        print("thats wrong")
                print(f"the correct answer was {actualAnswer}")
                print(f"your current score is {self.score}/{self.question_number}")
                print()
                
                
        def start_quiz(self):
                for _ in range(len(self.list)):
                        self.checkIfCorrect()