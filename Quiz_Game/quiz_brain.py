# all of the quiz functionality we are going to put it in quiz brain, 
# this is where all  the logic happens
import random

class QuizBrain:
    def __init__(self, quiz_bank):
        self.question_number = 0
        self.quiz_bank = quiz_bank
        self.score = 0

    def still_has_question(self):
        # check if quiz_bank still has questions
        # print('------------------')
        # print('LIST OF ALL THE ITEMS IN A  LIST :', self.quiz_bank)
        return True if self.question_number < len(self.quiz_bank) else False

    def next_question(self):
        # Go through the quiz bank, and each time ask question one by one
        # and check if the answer is correct or not if the answer
        # is correct increase true counter else increase false counter
        current_question = self.quiz_bank[self.question_number]
        self.question_number += 1

        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False): ")
        if user_answer == current_question.answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        
        print("The correct answer was: ", current_question.answer)
        print(f"Your current score is: {self.score}/{self.question_number}")


