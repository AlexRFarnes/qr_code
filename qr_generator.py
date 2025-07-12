# qr_generator.py

# qr_generator.py

import tkinter as tk

import customtkinter as ctk
from PIL import Image, ImageTk


class App(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("light")
        super().__init__(fg_color="white")

        self.title("")
        self.geometry("400x400")
        self.iconbitmap("empty.ico")

        self.mainloop()


App()
