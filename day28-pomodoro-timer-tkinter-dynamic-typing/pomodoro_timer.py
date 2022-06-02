from cgitb import reset
from tabnanny import check
import math
import tkinter as tk
from pathlib import Path


# ---------------------------- CONSTANTS ---------------------------------
PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
PARENT_DIR = str(Path(__file__).parent.resolve())

reps = 0
timer = None
# ---------------------------- TIMER RESET -------------------------------


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    checkmark_label.config(text='')

    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ---------------------------
def start_timer():
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    global reps
    reps += 1

    if reps % 2 != 0:
        count_down(work_sec)
        title_label.config(text='Work!', fg=RED)
    elif reps == 8:
        count_down(long_break_sec)
        title_label.config(text='Relax', fg=GREEN)
    else:
        count_down(short_break_sec)
        title_label.config(text='Short Break', fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM -----------------------
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = '0' + str(count_sec)

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmark_label.config(text=(reps//2) * '✓')


# ---------------------------- UI SETUP ----------------------------------
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_png = tk.PhotoImage(file=(PARENT_DIR+'/tomato.png'))
canvas.create_image(100, 112, image=tomato_png)

timer_text = canvas.create_text(
    100, 130, text='00:00',
    fill='white', font=(FONT_NAME, 35, 'bold')
    )
canvas.grid(row=1, column=1)

title_label = tk.Label(
    text='Timer', fg=GREEN, bg=YELLOW,
    font=(FONT_NAME, 48, 'bold')
    )
title_label.grid(row=0, column=1)

checkmark_label = tk.Label(
    fg=GREEN, bg=YELLOW,
    font=(FONT_NAME, 36, 'bold')
    )
checkmark_label.grid(row=3, column=1)

start_button = tk.Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text='Reset', command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
