import tkinter as tk
from tkinter import messagebox
from pathlib import Path
from random import choice, randint, shuffle


PARENT_DIR = str(Path(__file__).parent.resolve())
DEFAULT_EMAIL = 'sample@email.com'


# --- PASSWORD GENERATOR ---
def generator():

    pass_entry.delete(0, 'end')

    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
        'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
        'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    [password_list.append(choice(letters)) for char in range(randint(8, 10))]
    [password_list.append(choice(symbols)) for char in range(randint(2, 4))]
    [password_list.append(choice(numbers)) for char in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)
    pass_entry.insert(0, password)


# --- SAVE PASSWORD ---
def save():

    website = web_entry.get()
    username = user_entry.get()
    password = pass_entry.get()

    if len(website) < 1 or len(username) < 1 or len(password) < 1:

        messagebox.showinfo(
            title='Invalid Input',
            message="Unable to save invalid input. \
            Please don't leave any fields empty!"
            )

    else:

        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered: \nEmail: {username} "
            f"\nPassword: {password} \nIs it ok to save?"
            )

        if is_ok:

            new_entry = f"{website} | {username} | {password}\n"

            with open((PARENT_DIR + '/data.txt'), 'a') as file:
                file.write(new_entry)

            web_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')

            messagebox.showinfo(
                title='Successful',
                message="New login has been succesfully saved!"
                )


# --- UI SETUP ---
window = tk.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=(200), highlightthickness=0)

logo_png = tk.PhotoImage(file=(PARENT_DIR+'/logo.png'))
canvas.create_image(100, 100, image=logo_png)

canvas.grid(row=0, column=1)

web_label = tk.Label(text='Website:')
user_label = tk.Label(text='Email/Username:')
pass_label = tk.Label(text='Password:')
web_label.grid(row=1, column=0)
user_label.grid(row=2, column=0)
pass_label.grid(row=3, column=0)

web_entry = tk.Entry(width=38)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

user_entry = tk.Entry(width=38)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.insert(0, DEFAULT_EMAIL)

pass_entry = tk.Entry(width=21)
pass_entry.grid(row=3, column=1)

gen_button = tk.Button(text='Generate Password', command=generator)
gen_button.grid(row=3, column=2)

add_button = tk.Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
