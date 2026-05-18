import customtkinter as ctk

class AuthFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#ffd0eb")
        self.master = master
        self.title = ctk.CTkLabel(self, text="Welcome to Lockly", font=ctk.CTkFont("Helvetica", size=30, weight="bold"), text_color=("#FF0077"))
        self.title.pack(pady=40)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=250)
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", width=250, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text="Login",bg_color="#4CAF50", fg_color="#4CAF50", hover_color="#45a049")
        self.login_button.pack(pady=10)

        self.register_button = ctk.CTkButton(self, text="Register",bg_color="#2196F3", fg_color="#2196F3", hover_color="#1976D2")
        self.register_button.pack(pady=10)

        self.message_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=12), text_color="red")
        self.message_label.pack(pady=20)