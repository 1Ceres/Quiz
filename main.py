from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
i = 0
for each in question_data:
    question_bank.append(Question(question_data[i]["text"], question_data[i]["answer"]))
    i += 1

q = QuizBrain(question_bank)
while(q.still_have_question()):
    q.next_question()
    print("\n")
print(f"Your final score is {q.point}/{q.question_number}")