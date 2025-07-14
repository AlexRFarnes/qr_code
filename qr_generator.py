# qr_generator.py

import tkinter as tk

import customtkinter as ctk
import qrcode
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
        self.entry_string = ctk.StringVar()
        self.entry_string.trace_add("write", self.create_qr)
        EntryField(self, self.entry_string)

        # QR code
        self.qr_image = QrImage(self)

        # Run
        self.mainloop()

    def create_qr(self, *args):
        current_text = self.entry_string.get()
        if current_text:
            self.raw_image = qrcode.make(current_text).resize((300, 300))
            self.image_tk = ImageTk.PhotoImage(self.raw_image)
            self.qr_image.update_image(self.image_tk)
        else:
            self.qr_image.clear()


class EntryField(ctk.CTkFrame):
    def __init__(self, parent, entry_string):
        super().__init__(master=parent, corner_radius=20, fg_color="#021fb3")
        self.place(relx=0.5, rely=1, relwidth=1, relheight=0.4, anchor="center")

        # Grid layout
        self.rowconfigure((0, 1), weight=1, uniform="a")
        self.columnconfigure(0, weight=1, uniform="a")

        # Sub Frame
        self.frame = ctk.CTkFrame(self, fg_color="transparent")
        # Sub grid layout
        self.frame.columnconfigure(0, weight=1, uniform="b")
        self.frame.columnconfigure(1, weight=4, uniform="b")
        self.frame.columnconfigure(2, weight=2, uniform="b")
        self.frame.columnconfigure(3, weight=1, uniform="b")
        self.frame.grid(row=0, column=0)

        # Widgets
        entry = ctk.CTkEntry(
            self.frame,
            fg_color="#2e54e8",
            border_width=0,
            text_color="#ffffff",
            textvariable=entry_string,
        )
        entry.grid(row=0, column=1, sticky="nsew")

        button = ctk.CTkButton(
            self.frame, text="Save", fg_color="#2e54e8", hover_color="#4266f1"
        )
        button.grid(row=0, column=2, sticky="nsew", padx=10)


class QrImage(tk.Canvas):
    def __init__(self, parent):
        super().__init__(
            master=parent,
            background="#ffffff",
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.place(relx=0.5, rely=0.4, width=300, height=300, anchor="center")

    def update_image(self, image_tk):
        self.clear()
        self.create_image(0, 0, image=image_tk, anchor="nw")

    def clear(self):
        self.delete("all")


App()
