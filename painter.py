import customtkinter as ctk
from PIL import Image, ImageTk

class Painter(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.canvas = ctk.CTkCanvas(self, width=800, height=600)
        self.canvas.pack(fill=ctk.BOTH, expand=True)

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)

    def start_drawing(self, event):
        self.canvas.data = {"start_x": event.x, "start_y": event.y}

    def draw(self, event):
        start_x = self.canvas.data["start_x"]
        start_y = self.canvas.data["start_y"]
        current_x = event.x
        current_y = event.y
        self.canvas.create_line(start_x, start_y, current_x, current_y, fill="black", width=2)

        self.canvas.data["start_x"] = current_x
        self.canvas.data["start_y"] = current_y

    
