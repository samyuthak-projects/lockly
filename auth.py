import customtkinter as ctk
import bcrypt

from storage import load_users, save_users
from dashboard import DashboardFrame

class AuthFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#ffd0eb")
        self.master = master
        self.users = load_users()
        self.title = ctk.CTkLabel(self, text="Welcome to Lockly", font=ctk.CTkFont("Helvetica", size=30, weight="bold"), text_color=("#FF0077"))
        self.title.pack(pady=40)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=250)
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", width=250, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text="Login",bg_color="#4CAF50", fg_color="#4CAF50", hover_color="#45a049", command=self.login)
        self.login_button.pack(pady=10)

        self.register_button = ctk.CTkButton(self, text="Register",bg_color="#2196F3", fg_color="#2196F3", hover_color="#1976D2", command=self.register)
        self.register_button.pack(pady=10)

        self.message_label = ctk.CTkLabel(self, text="", font=ctk.CTkFont(size=12), text_color="red")
        self.message_label.pack(pady=20)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" or password == "":
            self.message_label.configure(text="Please fill in all fields!")
            return

        if username in self.users:
            self.message_label.configure(text="Username already exists!")
            return

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        self.users[username] = {"password": hashed_password, "vault": []}
        save_users(self.users)
        self.message_label.configure(text="Account created successfully!", text_color="green")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "" or password == "":
            self.message_label.configure(text="Please fill in all fields!")
            return

        if username not in self.users:
            self.message_label.configure(text="Invalid username!", text_color="red")
            return

        stored_hash = self.users[username]["password"].encode()
        if bcrypt.checkpw(password.encode(), stored_hash):
            self.master.switch_frame(DashboardFrame, username)
        else:
            self.message_label.configure(text="Invalid password!", text_color="red")