
import customtkinter as ctk
from backend import Task

class TaskCard(ctk.CTkFrame):
    """
    Description: Visual template based on a frame, deesigned with the ui elemts required for a task overview while searching for tasks

    Attributes:
        Class Attributes:
        Instance Attributes:
            parent_frame(ctk.CTkFrame): This represents the framethat the task card is located in
            task_obj(Task): The specific task the card is showing
    """
    def __init__(self, parent_frame: ctk.CTkFrame, task_obj: Task):
        super().__init__(parent_frame)
        self.task_obj = task_obj
        self.name_label = ctk.CTkLabel(self, text = str(self.task_obj.name))
        self.name_label.grid(row=0, column=0)
        self.due_date_label = ctk.CTkLabel(self, text = str(self.task_obj.due_date))
        self.due_date_label.grid(row=0, column=1)
        self.configure_button = ctk.CTkButton(self, text="Configure", command=lambda: print(f"Configuring {self.task_obj.name}"))
        self.configure_button.grid(row=0, column=2)