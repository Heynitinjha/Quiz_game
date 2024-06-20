from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

Question_Bank = []
for question in question_data:
    Question_text = question["text"]
    Question_answer = question["answer"]
    New_Question = Question(Question_text,Question_answer)
    Question_Bank.append(New_Question)

quiz = QuizBrain(Question_Bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the game")
print(f"Your final score is {quiz.score}/{quiz.question_number}")

