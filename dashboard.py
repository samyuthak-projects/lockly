import customtkinter as ctk

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master, username):
        super().__init__(master, fg_color="#ffd0eb")
        self.username = username
        self.title = ctk.CTkLabel(self, text=f"Welcome, {self.username}!", font=ctk.CTkFont("Helvetica", size=28, weight="bold"), text_color=("#FF0077"))
        self.title.pack(pady=40)

        self.subtitle = ctk.CTkLabel(self, text="Secure Credential Vault", font=ctk.CTkFont(size=18))
        self.subtitle.pack(pady=5)

        self.vault_frame = ctk.CTkFrame(self, fg_color="#ffe0f0")
        self.vault_frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.logout_button = ctk.CTkButton(self, text="Logout", bg_color="#f44336", fg_color="#f44336", hover_color="#d32f2f", command=self.logout)
        self.logout_button.pack(pady=10)

    def logout(self):
        self.master.show_auth()