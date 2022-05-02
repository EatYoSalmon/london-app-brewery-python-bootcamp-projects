import random
import hangman_art as ha
import hangman_words as hw
from replit import clear

print(ha.logo)
chosen_word = random.choice(hw.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed {guess}")
        
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:

        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")
    print(ha.stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win.")
