import customtkinter as ctk
from auth import AuthFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Lockly")
        self.geometry("700x500")
        self.current_frame = None
        self.show_auth()

    def switch_frame(self, frame_class, *args):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self, *args)
        self.current_frame.pack(fill="both", expand=True)

    def show_auth(self):
        self.switch_frame(AuthFrame)