import customtkinter as ctk

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master, username):
        super().__init__(master, fg_color="#ffd0eb")
        self.username = username
        self.title = ctk.CTkLabel(self, text=f"Welcome, {self.username}!", font=ctk.CTkFont("Helvetica", size=28, weight="bold"), text_color=("#FF0077"))
        self.title.pack(pady=40)