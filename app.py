import customtkinter as ctk
from auth import AuthFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Lockly")
        self.geometry("700x500")
        current_frame = None
        self.show_auth()

    def switch_frame(self, frame_class, *args):
        if current_frame is not None:
            current_frame.destroy()
        current_frame = frame_class(self, *args)
        current_frame.pack(fill="both", expand=True)

    def show_auth(self):
        self.switch_frame(AuthFrame)