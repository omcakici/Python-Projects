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
