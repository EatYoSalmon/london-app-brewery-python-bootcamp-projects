import requests
import tkinter as tk
from pathlib import Path


def get_quote():
    response = requests.get(url='https://api.kanye.rest')
    response.raise_for_status()

    data = response.json()

    quote = data['quote']
    canvas.itemconfig(quote_text, text=f'"{quote}"')


PARENT_DIR = str(Path(__file__).parent.resolve())
BACKGROUND = f'{PARENT_DIR}/background.png'
KANYE_MEMOJI = f'{PARENT_DIR}/kanye.png'
FONT = ('Arial', 30, 'bold')

window = tk.Tk()
window.title('Kanye Says...')
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=300, height=414)
background_img = tk.PhotoImage(file=BACKGROUND)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150, 207, text='Kanye Quote Goes HERE', width=250,
    font=FONT, fill='white')
canvas.grid(row=0, column=0)

kanye_img = tk.PhotoImage(file=KANYE_MEMOJI)
kanye_button = tk.Button(
    image=kanye_img,
    highlightthickness=0,
    command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
