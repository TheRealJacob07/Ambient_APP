import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import main

def save_settings():
    pass

def close_application():
    save_settings()
    root.destroy()

def about_application():
    messagebox.showinfo("About", "Windows Application Created Using Python")

root = tk.Tk()
root.title("Windows Application")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=close_application)

help_menu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about_application)

# create the widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Enter your name:").grid(row=0, column=0, sticky=tk.W)

entry = ttk.Entry(frame)
entry.grid(row=0, column=1, sticky=(tk.W, tk.E))

button = ttk.Button(frame, text="Submit", command=lambda: on_submit(entry.get()))
button.grid(row=0, column=2, sticky=(tk.W, tk.E))

root.mainloop()