import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import colorchooser

class App(ctk.CTk):

    def __init__(self, title):

        # setup
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.geometry('800x600')
        self.title(title)
        self.minsize(800,600)

        # widgets
        self.painter = Painter(self)

        # run
        self.mainloop()

class Painter(ctk.CTkFrame):
        
    # maybe add default settings here

    def __init__(self, parent):
        super().__init__(parent)
        self.pack()

        self.canvas = ctk.CTkCanvas(self, width = 400, height = 400)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

        self.selected_color = "black"

        self.create_drawing_options()
    
    def create_drawing_options(self):
        self.frame = ctk.CTkFrame(self.master)
        self.frame.pack()
    
        black_button = ctk.CTkButton(self.frame, text = 'Black', command = lambda: self.select_color("black"))
        black_button.pack()
    
        red_button = ctk.CTkButton(self.frame, text = 'Red', command = lambda: self.select_color("red"))
        red_button.pack()    

        color_button = ctk.CTkButton(self.frame, text='choose color', command = self.choose_color)
        color_button.pack()
        
    def select_color(self, color):
        global selected_color
        self.selected_color = color

    def choose_color(self):
        global selected_color
        self.selected_color = colorchooser.askcolor(title='Choose color')[1]

    def start_drawing(self, event):
        self.canvas.data = {"start_x": event.x, "start_y": event.y}
        self.canvas.bind("<B1-Motion>", self.draw)

    def draw(self, event):
        start_x = self.canvas.data["start_x"]
        start_y = self.canvas.data["start_y"]
        current_x = event.x
        current_y = event.y
        self.canvas.create_line(start_x, start_y, current_x, current_y, fill=self.selected_color, width=2)

        # Update the starting position for the next segment
        self.canvas.data["start_x"] = current_x
        self.canvas.data["start_y"] = current_y


App('draw-a-playlist')