import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("800x600")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "choices": ["Berlin", "Madrid", "Paris", "Rome"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "choices": ["Mars", "Venus", "Jupiter", "Saturn"],
                "correct_answer": "Mars"
            },
            {
                "question": "What is the largest mammal?",
                "choices": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
                "correct_answer": "Blue Whale"
            },
            {
                "question": "In which year did World War II end?",
                "choices": ["1943", "1945", "1950", "1939"],
                "correct_answer": "1945"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "choices": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
                "correct_answer": "William Shakespeare"
            },
            {
                "question": "What is the largest ocean?",
                "choices": ["Atlantic Ocean", "Indian Ocean", "Southern Ocean", "Pacific Ocean"],
                "correct_answer": "Pacific Ocean"
            }
        ]

        self.score = 0
        self.current_question_index = 0

        self.create_widgets()

    def create_widgets(self):
        style = ThemedStyle(self.root)
        style.set_theme("plastik")  # You can change this to another theme

        self.welcome_label = ttk.Label(self.root, text="Welcome to the Quiz Game!\nAnswer the following questions and test your knowledge.", wraplength=750, font=('Helvetica', 16))
        self.welcome_label.pack(pady=20)

        self.enter_game_button = ttk.Button(self.root, text="Enter Game", style="EnterGame.TButton", command=self.start_game)
        self.enter_game_button.pack(pady=10)

        self.question_label = ttk.Label(self.root, text="", font=('Helvetica', 20, 'bold'))
        self.question_label.pack(pady=20)

        self.choice_buttons = []
        for i in range(4):
            choice_button = ttk.Button(self.root, text="", style="ChoiceButton.TButton", command=self.set_user_answer)
            self.choice_buttons.append(choice_button)
            choice_button.pack(pady=5, padx=20)
            choice_button.bind("<Enter>", lambda event, button=choice_button: self.on_hover(event, button))
            choice_button.bind("<Leave>", lambda event, button=choice_button: self.on_leave(event, button))

        self.next_button = ttk.Button(self.root, text="Next", command=self.next_question, style="NextButton.TButton")
        self.previous_button = ttk.Button(self.root, text="Previous", command=self.previous_question, style="PreviousButton.TButton")
        self.submit_button = ttk.Button(self.root, text="Submit", command=self.submit_quiz, style="SubmitButton.TButton")
        self.feedback_label = ttk.Label(self.root, text="", font=('Helvetica', 14))
        self.final_results_label = ttk.Label(self.root, text="", font=('Helvetica', 24, 'bold'))
        self.play_again_button = ttk.Button(self.root, text="Play Again", command=self.reset_quiz, style="PlayAgainButton.TButton")

        self.show_welcome()

    def start_game(self):
        self.enter_game_button.pack_forget()
        self.show_question()

    def show_question(self):
        question = self.questions[self.current_question_index]
        self.question_label.config(text=question["question"])
        for i, choice in enumerate(question["choices"]):
            self.choice_buttons[i].config(text=choice, command=lambda c=choice: self.choice_var.set(c))

        self.question_label.pack(pady=20)
        for button in self.choice_buttons:
            button.pack(pady=5)

        if self.current_question_index == 0:
            self.next_button.pack(pady=20)
        else:
            self.previous_button.pack(pady=20)

        if self.current_question_index == len(self.questions) - 1:
            self.submit_button.pack(pady=20)

    def show_feedback(self, is_correct):
        feedback_text = "Correct! Well done!" if is_correct else f"Sorry, that's incorrect. The correct answer is: {self.questions[self.current_question_index]['correct_answer']}"
        self.feedback_label.config(text=feedback_text)
        self.feedback_label.pack(pady=10)

    def show_final_results(self):
        self.final_results_label.config(text=f"You've completed the quiz!\nYour final score is: {self.score}/{len(self.questions)}")
        if self.score == len(self.questions):
            self.final_results_label.config(text="Congratulations! You got all the questions right. You're a quiz master!")
        elif self.score >= len(self.questions) / 2:
            self.final_results_label.config(text="Good job! You know your stuff.")
        else:
            self.final_results_label.config(text="Keep learning. You'll get better!")
        self.final_results_label.pack(pady=20)
        self.play_again_button.pack(pady=20)

    def on_hover(self, event, button):
        button["style"] = "Hover.TButton"

    def on_leave(self, event, button):
        button["style"] = "ChoiceButton.TButton"

    def set_user_answer(self):
        user_answer = self.choice_var.get()
        correct_answer = self.questions[self.current_question_index]["correct_answer"]
        is_correct = user_answer.lower() == correct_answer.lower()
        self.score += 1 if is_correct else 0
        self.show_feedback(is_correct)

    def next_question(self):
        self.current_question_index += 1
        self.show_question()

    def previous_question(self):
        self.current_question_index -= 1
        self.show_question()

    def submit_quiz(self):
        self.show_final_results()

    def reset_quiz(self):
        self.score = 0
        self.current_question_index = 0
        self.show_welcome()

    def show_welcome(self):
        self.welcome_label.pack()
        self.enter_game_button.pack(pady=20)
        self.question_label.pack_forget()
        for button in self.choice_buttons:
            button.pack_forget()
        self.next_button.pack_forget()
        self.previous_button.pack_forget()
        self.submit_button.pack_forget()
        self.feedback_label.pack_forget()
        self.final_results_label.pack_forget()
        self.play_again_button.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    app.root.mainloop()
