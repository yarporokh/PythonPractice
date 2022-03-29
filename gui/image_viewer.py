import os
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

images = []
image_count = 0


def open_image():
    global label
    f_types = [('PNG/JPG Files', '*.png; *jpg')]
    file = tk.filedialog.askopenfilename(filetypes=f_types)

    if len(file) == 0:
        return

    img = Image.open(file)
    img = img.resize((500, 500))
    tkimage = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tkimage)
    label.image = tkimage
    label.grid(row=1, column=0, columnspan=3)


def open_dir():
    global label
    global images
    global image_count
    images = []
    image_count = 0
    directory = tk.filedialog.askdirectory()

    if len(directory) == 0:
        return

    for file in os.listdir(directory):
        if file.endswith(".jpg") or file.endswith(".png"):
            images.append(f"{directory}/{file}")

    load_image()


def load_image():
    global label
    global images
    global image_count
    global next_button
    global back_button

    img = Image.open(images[image_count])
    img = img.resize((500, 500))
    tkimage = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tkimage)
    label.image = tkimage
    label.grid(row=1, column=0, columnspan=3)

    if len(images) > 1 and image_count < len(images) - 1:
        next_button = ttk.Button(root, text="Next", command=lambda: change_image(1))
    else:
        next_button = ttk.Button(root, text="Next", state=tk.DISABLED)

    if image_count == 0:
        back_button = ttk.Button(root, text="Back", state=tk.DISABLED)
    else:
        back_button = ttk.Button(root, text="Back", command=lambda: change_image(-1))

    back_button.grid(row=5, column=0)
    next_button.grid(row=5, column=1)


def change_image(n):
    global image_count
    image_count += n
    load_image()


root = tk.Tk()
root.title("Image Viewer")
root.geometry("500x550")
root.resizable(False, False)

menubar = tk.Menu()
root.config(menu=menubar)
root.option_add("*tearOff", False)

file_menu = tk.Menu(menubar)

menubar.add_cascade(label="Open", menu=file_menu)
file_menu.add_command(label="Open dir", command=open_dir)
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
