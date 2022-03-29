import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Image Viewer")

menubar = tk.Menu()
root.config(menu=menubar)
root.option_add("*tearOff", False)

file_menu = tk.Menu(menubar)

menubar.add_cascade(label="Open", menu=file_menu)
file_menu.add_command(label="Open dir")
file_menu.add_command(label="Open image")

root.mainloop()
