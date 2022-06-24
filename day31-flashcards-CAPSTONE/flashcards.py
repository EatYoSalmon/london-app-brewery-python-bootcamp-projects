from curses import flash
from pathlib import Path
import tkinter as tk
import json
from numpy import flip
import pandas as pd
from random import choice

# --- CONSTANTS ---
PARENT_DIR = str(Path(__file__).parent.resolve())
IMAGES_DIR = PARENT_DIR + '/images'
DATA_DIR = PARENT_DIR + '/data'

BACKGROUND_COLOR = '#B1DDC6'
FONT = {
    'title': ('Ariel', 40, 'italic'),
    'word': ('Ariel', 60, 'bold'),
}

# --- DEPENDENCIES ---
try:
    df = pd.read_csv(DATA_DIR + '/words_to_learn.csv')

except FileNotFoundError:
    df = pd.read_csv(DATA_DIR + '/french_words.csv')

finally:
    flashcards = df.to_dict(orient='records')
    current_card = {}


# --- FUNCTIONS ---
def flip_card():
    global current_card

    card.itemconfig(card_image, image=card_back_png)
    card.itemconfig(card_title, text='English', fill='white')
    card.itemconfig(card_word, text=current_card['English'], fill='white')


def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = choice(flashcards)

    card.itemconfig(card_image, image=card_front_png)
    card.itemconfig(card_title, text='French', fill='black')
    card.itemconfig(card_word, text=current_card['French'], fill='black')

    flip_timer = window.after(3000, flip_card)


def remove_card():
    global current_card

    flashcards.remove(current_card)
    next_card()


# --- USER INTERFACE ---
window = tk.Tk()
window.title("Flashy 💅🏻✨")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(0, next_card)

card = tk.Canvas(
    width=800, height=526,
    highlightthickness=0, bg=BACKGROUND_COLOR
)

card_back_png = tk.PhotoImage(file=(IMAGES_DIR+'/card_back.png'))
card_front_png = tk.PhotoImage(file=(IMAGES_DIR+'/card_front.png'))

card_image = card.create_image((800/2), (526/2), image=card_front_png)

card_title = card.create_text(
    400, 150, text='Title',
    fill='black', font=FONT['title']
)
card_word = card.create_text(
    400, 263, text='Word',
    fill='black', font=FONT['word']
)

card.grid(row=0, column=0, columnspan=2)

right_png = tk.PhotoImage(file=(IMAGES_DIR+'/right.png'))
right_button = tk.Button(
    image=right_png, bg=BACKGROUND_COLOR,
    highlightthickness=0, border=0,
    command=remove_card
)
right_button.grid(row=1, column=1)

wrong_png = tk.PhotoImage(file=(IMAGES_DIR+'/wrong.png'))
wrong_button = tk.Button(
    image=wrong_png, bg=BACKGROUND_COLOR,
    highlightthickness=0, border=0,
    command=next_card
)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()

# --- UPDATE LIST OF WORDS TO LEARN ---
french_words = []
english_words = []

for card in flashcards:
    french_words.append(card['French'])
    english_words.append(card['English'])

flashcards_to_learn = {
    'French': french_words,
    'English': english_words
}

df = pd.DataFrame.from_dict(flashcards_to_learn)
df.to_csv(DATA_DIR + '/words_to_learn.csv')
