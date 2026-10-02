import tkinter as tk
from tkinter import messagebox
import os


class QuizSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz System")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#0F172A")

        # Theme colors
        self.bg = "#0F172A"
        self.card = "#1E293B"
        self.primary = "#6366F1"
        self.primary_hover = "#4F46E5"
        self.text = "#F8FAFC"
        self.secondary = "#CBD5E1"
        self.success = "#22C55E"
        self.danger = "#EF4444"
        self.input_bg = "#334155"

        self.questions = []
        self.current_question = 0
        self.score = 0
        self.name = ""
        self.filename = ""

        self.show_main_menu()

    # ---------------- CLEAR SCREEN ----------------

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ---------------- BUTTON STYLE ----------------

    def create_button(self, text, command, width=22):
        button = tk.Button(
            self.root,
            text=text,
            command=command,
            font=("Segoe UI", 13, "bold"),
            width=width,
            height=2,
            bg=self.primary,
            fg="white",
            activebackground=self.primary_hover,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            bd=0
        )

        button.pack(pady=8)

        return button

    # ---------------- TITLE ----------------

    def create_title(self, text, size=30):
        tk.Label(
            self.root,
            text=text,
            font=("Segoe UI", size, "bold"),
            bg=self.bg,
            fg=self.text
        ).pack(pady=(30, 10))

    # ---------------- MAIN MENU ----------------

    def show_main_menu(self):
        self.clear_screen()

        tk.Label(
            self.root,
            text="QUIZ SYSTEM",
            font=("Segoe UI", 32, "bold"),
            bg=self.bg,
            fg=self.text
        ).pack(pady=(60, 5))

        tk.Label(
            self.root,
            text="Test your knowledge and track your score",
            font=("Segoe UI", 13),
            bg=self.bg,
            fg=self.secondary
        ).pack(pady=(0, 40))

        self.create_button(
            "▶  Start Quiz",
            self.select_subject
        )

        self.create_button(
            "▣  View Results",
            self.view_result
        )

        self.create_button(
            "✕  Exit",
            self.root.destroy
        )

        tk.Label(
            self.root,
            text="Python • English • Maths",
            font=("Segoe UI", 10),
            bg=self.bg,
            fg="#64748B"
        ).pack(pady=30)

    # ---------------- SUBJECT SELECTION ----------------

    def select_subject(self):
        self.clear_screen()

        self.create_title("Select Subject", 28)

        tk.Label(
            self.root,
            text="Choose a subject to begin your quiz",
            font=("Segoe UI", 12),
            bg=self.bg,
            fg=self.secondary
        ).pack(pady=(0, 25))

        self.create_button(
            "Python",
            lambda: self.start_quiz("python.txt")
        )

        self.create_button(
            "English",
            lambda: self.start_quiz("english.txt")
        )

        self.create_button(
            "Maths",
            lambda: self.start_quiz("maths.txt")
        )

        back = tk.Button(
            self.root,
            text="← Back",
            font=("Segoe UI", 11),
            bg=self.bg,
            fg=self.secondary,
            activebackground=self.bg,
            activeforeground=self.text,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.show_main_menu
        )

        back.pack(pady=20)

    # ---------------- START QUIZ ----------------

    def start_quiz(self, filename):

        self.filename = filename

        if not os.path.exists(filename):
            messagebox.showerror(
                "Error",
                f"{filename} not found!"
            )
            return

        self.questions = []

        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()

                    if "|" in line:
                        question, answer = line.split("|", 1)

                        self.questions.append(
                            (question.strip(), answer.strip())
                        )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Could not read file:\n{e}"
            )
            return

        if len(self.questions) == 0:
            messagebox.showerror(
                "Error",
                "No questions found!"
            )
            return

        self.ask_name()

    # ---------------- NAME ----------------

    def ask_name(self):

        self.clear_screen()

        self.create_title("Welcome to the Quiz", 28)

        tk.Label(
            self.root,
            text="Enter your name to get started",
            font=("Segoe UI", 13),
            bg=self.bg,
            fg=self.secondary
        ).pack(pady=(0, 25))

        self.name_entry = tk.Entry(
            self.root,
            font=("Segoe UI", 14),
            width=32,
            bg=self.input_bg,
            fg=self.text,
            insertbackground="white",
            relief="flat",
            justify="center"
        )

        self.name_entry.pack(ipady=10, pady=10)

        self.create_button(
            "Start Quiz",
            self.begin_quiz,
            18
        )

        back = tk.Button(
            self.root,
            text="← Back",
            font=("Segoe UI", 11),
            bg=self.bg,
            fg=self.secondary,
            activebackground=self.bg,
            activeforeground=self.text,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.select_subject
        )

        back.pack(pady=15)

    # ---------------- BEGIN QUIZ ----------------

    def begin_quiz(self):

        self.name = self.name_entry.get().strip()

        if self.name == "":
            messagebox.showwarning(
                "Warning",
                "Please enter your name."
            )
            return

        self.current_question = 0
        self.score = 0

        self.show_question()

    # ---------------- QUESTIONS ----------------

    def show_question(self):

        self.clear_screen()

        question, answer = self.questions[
            self.current_question
        ]

        # Progress
        tk.Label(
            self.root,
            text=f"QUESTION {self.current_question + 1} "
                 f"OF {len(self.questions)}",
            font=("Segoe UI", 11, "bold"),
            bg=self.bg,
            fg=self.primary
        ).pack(pady=(35, 15))

        # Question card
        question_frame = tk.Frame(
            self.root,
            bg=self.card,
            width=700,
            height=170
        )

        question_frame.pack(pady=15)
        question_frame.pack_propagate(False)

        tk.Label(
            question_frame,
            text=question,
            font=("Segoe UI", 18, "bold"),
            bg=self.card,
            fg=self.text,
            wraplength=620,
            justify="center"
        ).place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        tk.Label(
            self.root,
            text="Enter your answer below",
            font=("Segoe UI", 11),
            bg=self.bg,
            fg=self.secondary
        ).pack(pady=(20, 5))

        self.answer_entry = tk.Entry(
            self.root,
            font=("Segoe UI", 14),
            width=45,
            bg=self.input_bg,
            fg=self.text,
            insertbackground="white",
            relief="flat",
            justify="center"
        )

        self.answer_entry.pack(ipady=10, pady=10)

        self.create_button(
            "Submit Answer  →",
            self.check_answer,
            20
        )

        self.answer_entry.focus()

        # Press Enter to submit answer
        self.answer_entry.bind(
            "<Return>",
            lambda event: self.check_answer()
        )

    # ---------------- CHECK ANSWER ----------------

    def check_answer(self):

        user_answer = self.answer_entry.get().strip()

        if user_answer == "":
            messagebox.showwarning(
                "Warning",
                "Please enter an answer."
            )
            return

        question, correct_answer = self.questions[
            self.current_question
        ]

        if user_answer.lower() == correct_answer.lower():

            self.score += 1

            messagebox.showinfo(
                "Correct!",
                "✓ Correct Answer!"
            )

        else:

            messagebox.showinfo(
                "Incorrect",
                f"✗ Wrong Answer!\n\n"
                f"Correct answer: {correct_answer}"
            )

        self.current_question += 1

        if self.current_question < len(self.questions):
            self.show_question()

        else:
            self.finish_quiz()

    # ---------------- FINISH QUIZ ----------------

    def finish_quiz(self):

        total = len(self.questions)

        percentage = (self.score / total) * 100

        if percentage >= 50:
            result = "PASS"
            result_color = self.success

        else:
            result = "FAIL"
            result_color = self.danger

        # Save result
        try:
            with open("result.txt", "a", encoding="utf-8") as file:

                file.write(f"Name: {self.name}\n")
                file.write(f"Subject: {self.filename}\n")
                file.write(f"Score: {self.score}/{total}\n")
                file.write(f"Percentage: {percentage:.2f}%\n")
                file.write(f"RESULT: {result}\n")
                file.write("----------------------\n")

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Could not save result:\n{e}"
            )

        self.clear_screen()

        tk.Label(
            self.root,
            text="QUIZ COMPLETED!",
            font=("Segoe UI", 30, "bold"),
            bg=self.bg,
            fg=self.text
        ).pack(pady=(50, 15))

        tk.Label(
            self.root,
            text=f"Well done, {self.name}!",
            font=("Segoe UI", 15),
            bg=self.bg,
            fg=self.secondary
        ).pack(pady=5)

        # Score card
        result_frame = tk.Frame(
            self.root,
            bg=self.card,
            width=500,
            height=200
        )

        result_frame.pack(pady=25)
        result_frame.pack_propagate(False)

        tk.Label(
            result_frame,
            text=f"Score: {self.score}/{total}",
            font=("Segoe UI", 18, "bold"),
            bg=self.card,
            fg=self.text
        ).pack(pady=(25, 5))

        tk.Label(
            result_frame,
            text=f"Percentage: {percentage:.2f}%",
            font=("Segoe UI", 16),
            bg=self.card,
            fg=self.secondary
        ).pack(pady=5)

        tk.Label(
            result_frame,
            text=result,
            font=("Segoe UI", 20, "bold"),
            bg=self.card,
            fg=result_color
        ).pack(pady=10)

        self.create_button(
            "← Back to Menu",
            self.show_main_menu,
            20
        )

    # ---------------- VIEW RESULTS ----------------

    def view_result(self):

        self.clear_screen()

        self.create_title("Previous Results", 28)

        text_box = tk.Text(
            self.root,
            width=65,
            height=17,
            font=("Consolas", 11),
            bg=self.card,
            fg=self.text,
            insertbackground="white",
            relief="flat",
            padx=15,
            pady=15
        )

        text_box.pack(pady=10)

        if os.path.exists("result.txt"):

            try:
                with open("result.txt", "r", encoding="utf-8") as file:
                    results = file.read()

                if results:
                    text_box.insert("1.0", results)

                else:
                    text_box.insert(
                        "1.0",
                        "No results available."
                    )

            except Exception as e:
                text_box.insert(
                    "1.0",
                    f"Could not read results:\n{e}"
                )

        else:

            text_box.insert(
                "1.0",
                "No results available."
            )

        text_box.config(state="disabled")

        back = tk.Button(
            self.root,
            text="← Back to Menu",
            font=("Segoe UI", 11, "bold"),
            bg=self.primary,
            fg="white",
            activebackground=self.primary_hover,
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            command=self.show_main_menu
        )

        back.pack(pady=15)


# ---------------- RUN APPLICATION ----------------

root = tk.Tk()

app = QuizSystem(root)

root.mainloop()
