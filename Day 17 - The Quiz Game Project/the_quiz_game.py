from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    q_object = Question(q["text"], q["answer"])
    question_bank.append(q_object)

is_new_game = True
while is_new_game:

    brain = QuizBrain(question_bank)
    is_game_over = False

    while (not is_game_over) and (brain.still_has_question()):
        is_game_over = brain.next_question()

    print(f"Final Score: {brain.score}")

    new_game = input("Do you want to play for another round? Enter 'y' to play again, or 'n' to quit: ")
    if new_game.lower() == "y":
        is_new_game = True
    else:
        is_new_game = False