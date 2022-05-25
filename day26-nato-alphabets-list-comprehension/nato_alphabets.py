# NATO Phoenetic Alphabets
# 1.Create a dictionary in this format:
#     {'A': 'Alfa', 'B': 'Bravo', ...}
# 2. Create a list of the phonetic code words from a word that the user input

from pathlib import Path
import pandas as pd


PARENT_DIR = str(Path(__file__).parent.resolve())
df = pd.read_csv(PARENT_DIR + '/nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = input("Enter a word: ").upper()
nato_phonetics = [nato_dict[letter] for letter in word]
print(nato_phonetics)
