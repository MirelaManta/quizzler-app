from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):   # declaring what data type quiz-brain is
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Trivia TF")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,   # added the width parameter so that the text could wrap onto canvas
            text="Question here.",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR)
        self.score_label.config(font=("Arial", 12, "bold"), fg="white")
        self.score_label.grid(column=1, row=0)

        img_true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=img_true, highlightthickness=0, pady=20, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        img_false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=img_false, highlightthickness=0, pady=20, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
