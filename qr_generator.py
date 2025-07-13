# qr_generator.py

import tkinter as tk

import customtkinter as ctk
from PIL import Image, ImageTk


class App(ctk.CTk):
    def __init__(self):
        # Window setup
        ctk.set_appearance_mode("light")
        super().__init__(fg_color="white")

        # Customization
        self.title("")
        self.geometry("400x400")
        self.iconbitmap("empty.ico")

        # Entry field
        EntryField(self)

        # Run
        self.mainloop()


class EntryField(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, corner_radius=20, fg_color="#021fb3")
        self.place(relx=0.5, rely=1, relwidth=1, relheight=0.4, anchor="center")

        # Grid layout
        self.rowconfigure((0, 1), weight=1, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")

        # Widgets
        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        self.frame.columnconfigure(0, weight=1, uniform="b")
        self.frame.columnconfigure(1, weight=4, uniform="b")
        self.frame.columnconfigure(2, weight=2, uniform="b")
        self.frame.columnconfigure(3, weight=1, uniform="b")
        self.frame.grid(row=0, column=0)

        entry = ctk.CTkEntry(
            self.frame, fg_color="#2e54e8", border_width=0, text_color="#ffffff"
        )
        entry.grid(row=0, column=1, sticky="nsew")

        button = ctk.CTkButton(
            self.frame, text="Save", fg_color="#2e54e8", hover_color="#4266f1"
        )
        button.grid(row=0, column=2, sticky="nsew", padx=10)


App()
