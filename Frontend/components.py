
import customtkinter as ctk
from backend import Task
from PIL import Image

class TaskCard(ctk.CTkFrame):
    """
    Description: Visual template based on a frame, deesigned with the ui elemts required for a task overview while searching for tasks

    Attributes:
        Class Attributes:
        Instance Attributes:
            parent_frame(ctk.CTkFrame): This represents the frame that the task card is located in
            task_obj(Task): The specific task the card is showing
    """
    def __init__(self, parent_frame: ctk.CTkFrame, task_obj: Task):
        super().__init__(parent_frame)
        self.task_obj = task_obj
        self.name_label = ctk.CTkLabel(self, text = str(self.task_obj.name), font = ctk.CTkFont("Inter", 20, "bold"))
        self.name_label.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        self.due_date_label = ctk.CTkLabel(self, text = f"Due: {str(self.task_obj._due_date)}")
        self.due_date_label.grid(row=2, column=0, sticky = "sw", padx=10, pady=10)
        self.duration_label= ctk.CTkLabel(self, text = f"Total Duration: {str(self.task_obj._duration)} Minutes")
        self.duration_label.grid(row=1, column=0,sticky="sw", padx=10, pady=10)
        self.icon_edit_dark = Image.open("assets/icons/dark/edit_dark.png")
        self.icon_edit_light = Image.open("assets/icons/light/edit_light.png")
        self.ctk_icon_edit = ctk.CTkImage(
            light_image=self.icon_edit_light, 
            dark_image=self.icon_edit_dark
                    )
        self.configure_button = ctk.CTkButton(self, image=self.ctk_icon_edit, text="Configure", command=lambda: print(f"Configuring {self.task_obj.name}"), anchor="w")
        self.configure_button.grid(row=2, column=1, sticky = "se", padx=10, pady=10)
