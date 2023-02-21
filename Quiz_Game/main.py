from question_model import Question
from api_call import ApiCall
from quiz_brain import QuizBrain
from arts import logo
import random

api_call = ApiCall()
print(logo)
print('SELECT CATEGORY ID FROM BELOW:')
print('--------------------------------')
api_call.get_category_data()
category_data = api_call.category_data

api_call.get_question_data()
question_data = api_call.question_data

question_bank = []

for q in question_data["results"]:
    text = q["question"]
    answer = q["correct_answer"]
    question = Question(text, answer)
    question_bank.append(question)

random.shuffle(question_bank)
quiz_logic = QuizBrain(question_bank)

## while quiz bank has still quesiton keep asking
while quiz_logic.still_has_question():
    quiz_logic.next_question()


