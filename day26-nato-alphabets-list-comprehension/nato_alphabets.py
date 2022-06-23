# NATO Phoenetic Alphabets
# 1.Create a dictionary in this format:
#     {'A': 'Alfa', 'B': 'Bravo', ...}
# 2. Create a list of the phonetic code words from a word that the user input

from pathlib import Path
import pandas as pd


PARENT_DIR = str(Path(__file__).parent.resolve())

df = pd.read_csv(PARENT_DIR + '/nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

looping = True
while looping:
    try:
        word = input("Enter a word: ").upper()
        nato_phonetics = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        looping = False
        print(nato_phonetics)
