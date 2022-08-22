import tkinter as tk
from pathlib import Path
from quiz_brain import QuizBrain


# --- CONSTANTS ---
PARENT_DIR = str(Path(__file__).parent.resolve())
IMAGES_DIR = f'{PARENT_DIR}/images'
THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

    # --- Row 0 ---
        self.score = tk.Label(
            fg='white', bg=THEME_COLOR,
            text='Score: 0'
        )
        self.score.grid(row=0, column=1)

    # --- Row 1 ---
        self.card = tk.Canvas(
            width=300, height=250,
            highlightthickness=0, bg='white',
        )

        self.q_text = self.card.create_text(
            150, 125,
            width=280,
            fill=THEME_COLOR, font=FONT,
            text='Hello World'
        )
        self.get_next_question()

        self.card.grid(row=1, column=0, columnspan=2, pady=50)

    # --- Row 2 ---
        right_png = tk.PhotoImage(file=f'{IMAGES_DIR}/true.png')
        self.rbutton = tk.Button(
            image=right_png, bg=THEME_COLOR,
            highlightthickness=0, border=0,
            command=self.answer_true
        )
        self.rbutton.grid(row=2, column=0)

        wrong_png = tk.PhotoImage(file=f'{IMAGES_DIR}/false.png')
        self.wbutton = tk.Button(
            image=wrong_png, bg=THEME_COLOR,
            highlightthickness=0, border=0,
            command=self.answer_false
        )
        self.wbutton.grid(row=2, column=1)

    # --- Main Loop ---
        self.window.mainloop()

# Methods
    def get_next_question(self):
        self.card.config(bg='white')
        self.score.config(text=f"Score: {self.quiz.score}")

        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.card.itemconfig(
                self.q_text, text=question_text
            )
        else:
            self.card.itemconfig(
                self.q_text, text="You've completed the quiz."
            )
            self.rbutton.config(state='disabled')
            self.wbutton.config(state='disabled')

    def answer_true(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        feedback = 'green' if is_right else 'red'
        self.card.config(bg=feedback)

        self.window.after(1000, self.get_next_question)
