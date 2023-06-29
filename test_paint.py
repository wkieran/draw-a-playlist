import tkinter as tk
import ttkbootstrap as ttk
from tkinter import colorchooser


# window
window = ttk.Window(themename="darkly")
window.title = ('draw-a-playlist')
window.geometry('800x600')
# window.configure(bg="black")


# title
title_label = ttk.Label(master = window, text='draw-a-playlist', font='calibri 24 bold')
title_label.pack(anchor='nw')

# canvas
def start_drawing(event):
    canvas.data = {"start_x": event.x, "start_y": event.y}
    canvas.bind("<B1-Motion>", draw)

def draw(event):
    start_x = canvas.data["start_x"]
    start_y = canvas.data["start_y"]
    current_x = event.x
    current_y = event.y
    canvas.create_line(start_x, start_y, current_x, current_y, fill=selected_color, width=2)

    # Update the starting position for the next segment
    canvas.data["start_x"] = current_x
    canvas.data["start_y"] = current_y

canvas = tk.Canvas(master= window, width=300, height=300, highlightthickness=2, highlightbackground="black")
canvas.configure(bg="white")
canvas.pack()

canvas.bind("<Button-1>", start_drawing)

# options bar
options_frame = ttk.Frame(master=window)
options_frame.pack(anchor='w')

selected_color = "black" # init

def select_color(color):
    global selected_color
    selected_color = color

def choose_color():
    global selected_color
    color_code = colorchooser.askcolor(title='Choose color')
    selected_color = color_code[1]

# Button styles
black_button = ttk.Button(options_frame, text='black', command=lambda: select_color("black"))
black_button.pack()

red_button = ttk.Button(options_frame, text='red', command=lambda: select_color("red"))
red_button.pack()

color_button = ttk.Button(options_frame, text='choose color', command = choose_color)
color_button.pack()

# export

# output

# run
window.mainloop()