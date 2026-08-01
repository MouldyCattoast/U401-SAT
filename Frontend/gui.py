import customtkinter as ctk
from backend import Task
from backend import TaskManager

class AephaseApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.title("Aephase")
        self.geometry("1000x600")

if __name__ == "__main__":
    app = AephaseApp()
    app.mainloop()
       