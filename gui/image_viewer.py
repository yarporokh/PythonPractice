import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Image Viewer")
root.geometry("500x500")

menubar = tk.Menu()
root.config(menu=menubar)
root.option_add("*tearOff", False)

file_menu = tk.Menu(menubar)

menubar.add_cascade(label="Open", menu=file_menu)
file_menu.add_command(label="Open dir")
file_menu.add_command(label="Open image")

img_frame = tk.Frame(root)
img_frame.pack(side="top")
btn_frame = tk.Frame(root)
btn_frame.pack(side="bottom")

back_button = ttk.Button(btn_frame, text="Back")

quit_button = ttk.Button(btn_frame, text="Quit", command=root.destroy)

next_button = ttk.Button(btn_frame, text="Next")

back_button.grid(row=0, column=1)
next_button.grid(row=0, column=2)
quit_button.grid(row=0, column=3)
root.mainloop()
