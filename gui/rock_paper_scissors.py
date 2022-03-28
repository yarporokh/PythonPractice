import random
import tkinter as tk
from tkinter import ttk

player_score = 0
computer_score = 0
CHOICES = ["rock", "paper", "scissors"]


def update_labels(p, c):
    scores_label.config(text=f"Your score: {player_score}"
                             f"\nComputer score: {computer_score}")
    choices_label.config(text=f"Your choice: {p}"
                              f"\nComputer choice: {c}")


def computer_choice():
    return random.choice(CHOICES)


def choose_rock():
    choice = computer_choice()
    if choice == "rock":
        pass
    elif choice == "paper":
        global computer_score
        computer_score += 1
    else:
        global player_score
        player_score += 1
    update_labels("rock", choice)


def choose_paper():
    choice = computer_choice()
    if choice == "rock":
        global player_score
        player_score += 1
    elif choice == "paper":
        pass
    else:
        global computer_score
        computer_score += 1
    update_labels("paper", choice)


def choose_scissors():
    choice = computer_choice()
    if choice == "rock":
        global computer_score
        computer_score += 1
    elif choice == "paper":
        global player_score
        player_score += 1
    else:
        pass
    update_labels("scissors", choice)


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("600x150")
root.resizable(False, False)

s = ttk.Style()
s.configure('TButton', font=('Helvetica', 24))
s.configure('TLabel', font=('Helvetica', 24))

buttons_frame = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
buttons_frame.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)
labels_frame = tk.Frame(root, relief=tk.RAISED, borderwidth=1)
labels_frame.pack(fill=tk.BOTH, expand=True, side=tk.RIGHT)

scores_label = ttk.Label(labels_frame,
                         text=f"Your score: {player_score}"
                              f"\nComputer score: {computer_score}",
                         style="TLabel")
scores_label.pack()

choices_label = ttk.Label(labels_frame,
                          text="Your choice: "
                               "\nComputer choice: ",
                          style="TLabel")
choices_label.pack()

rock_button = ttk.Button(buttons_frame, text="Rock", command=choose_rock, style="TButton")
rock_button.pack()

paper_button = ttk.Button(buttons_frame, text="Paper", command=choose_paper, style="TButton")
paper_button.pack()

scissors_button = ttk.Button(buttons_frame, text="Scissors", command=choose_scissors, style="TButton")
scissors_button.pack()

root.mainloop()
