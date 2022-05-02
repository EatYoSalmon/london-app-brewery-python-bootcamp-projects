class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_question(self):
        """This method checks whether if there are still questions left unasked
        within the list; it returns True if yes, and False if there aren't any questions left."""

        number = self.question_number
        last_question = len(self.question_list)
        if number < last_question:
            return True
        else:
            print("\nWow! You little nerd! You got full score!")
            return False

    def next_question(self):
        """This method asks the player to input their answer to the question;
        Returns the result of whether if the game is over."""

        current_question = self.question_list[self.question_number]
        self.question_number += 1

        player_answer = input(f"\nQ.{self.question_number}: {current_question.text} (True/False): ")
        correct_answer = current_question.answer

        is_game_over = self.check_answer(player_answer, correct_answer)
        return is_game_over

    def check_answer(self, player_answer, correct_answer):
        """Checks if the player answered the question correctly;
        Returns False to var`is_game_over` if correct; returns True if incorrect"""

        if player_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            result = False
        else:
            print("Oh no! You guessed wrong.")
            print(f"The correct answer was '{correct_answer}'.")
            result = True

        print(f"Current Score: {self.score}")
        return result
