import customtkinter as ctk

class AuthFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title = ctk.CTkLabel(self, text="Welcome to Lockly", font=ctk.CTkFont(size=30, weight="bold"))
        self.title.pack(pady=40)        