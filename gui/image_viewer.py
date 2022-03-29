import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


def open_image():
    global label
    f_types = [('PNG/JPG Files', '*.png; *jpg')]
    file = tk.filedialog.askopenfilename(filetypes=f_types)
    img = Image.open(file)
    img = img.resize((500, 500))
    tkimage = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tkimage)
    label.image =tkimage
    label.grid(row=1, column=0, columnspan=3)

root = tk.Tk()
root.title("Image Viewer")
root.geometry("500x550")
root.resizable(False, False)

menubar = tk.Menu()
root.config(menu=menubar)
root.option_add("*tearOff", False)

file_menu = tk.Menu(menubar)

menubar.add_cascade(label="Open", menu=file_menu)
file_menu.add_command(label="Open dir")
file_menu.add_command(label="Open image", command=open_image)


label = tk.Label(text="No Image")
label.grid(row=1, column=0, columnspan=3)

back_button = ttk.Button(root, text="Back", state=tk.DISABLED)
quit_button = ttk.Button(root, text="Quit", command=root.destroy)
next_button = ttk.Button(root, text="Next", state=tk.DISABLED)

back_button.grid(row=5, column=0)
next_button.grid(row=5, column=1)
quit_button.grid(row=5, column=2)
root.mainloop()
