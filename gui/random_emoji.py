import random
import tkinter as tk
from tkinter import ttk


def change(l):
    emojis = ["❤", "😊", "😂", "🤣", "😍", "😒",
              "👌", "😘", "😁", "🐱", "‍🐉", "✔",
              "🎉", "🌹", "💋", "👏", "😃"]
    l.config(text=random.choice(emojis), font=("", 120))


root = tk.Tk()
root.geometry("500x500")
root.resizable(0, 0)

label = ttk.Label(root, text="Emoji", font=("", 120))
emoji_button = ttk.Button(root, text="Random emoji", command=lambda: change(label))
quit_button = ttk.Button(root, text="Quit", command=root.destroy)

label.pack(side="top", expand=True)
emoji_button.pack(side="left", expand=True, fill=tk.BOTH)
quit_button.pack(side="right", expand=True, fill=tk.BOTH)

root.mainloop()
