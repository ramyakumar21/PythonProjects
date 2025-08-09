from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
    question = x["question"]
    answer = x["correct_answer"]
    new_question = Question(question, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.user_score}/{quiz.question_number}")

