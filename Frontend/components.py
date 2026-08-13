# ==============================================================================
# @file:        components.py
# @author:      mouldycattoast
# ==============================================================================
"""
This module provides any custom-made GUI elements that can be used throughout the application
"""

import customtkinter as ctk
from backend import Task
from PIL import Image

class TaskCard(ctk.CTkFrame):
    """
    Description: Visual template based on a frame, designed with the ui elemts required for a task overview while searching for tasks

    Attributes:
        Class Attributes:
        Instance Attributes:
            parent_frame(ctk.CTkFrame): This represents the frame that the task card is located in
            task_obj(Task): The specific task the card is showing
    """
    def __init__(self, parent_frame: ctk.CTkFrame, task_obj: Task, on_delete_callback=None, on_modify_callback=None):
        super().__init__(parent_frame)
        self.task_obj = task_obj
        self.on_delete_callback = on_delete_callback
        self.on_modify_callback = on_modify_callback
        self.name_label = ctk.CTkLabel(self, text = str(self.task_obj.name), font = ctk.CTkFont("Inter", 25, "bold"))
        self.name_label.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        self.due_date_label = ctk.CTkLabel(self, text = f"Due: {str(self.task_obj._due_date)}")
        self.due_date_label.grid(row=2, column=0, sticky = "sw", padx=10, pady=10)

        if self.task_obj._duration:
            self.duration_label= ctk.CTkLabel(self, text = f"Total Duration: {str(self.task_obj._duration)} Minutes")
        else:
            self.duration_label= ctk.CTkLabel(self, text = f"Total Duration: {str(self.task_obj._duration)}")
        self.duration_label.grid(row=1, column=0,sticky="sw", padx=10, pady=10)
        self.icon_delete_dark = Image.open("assets/icons/dark/delete_dark.png")
        self.icon_delete_light = Image.open("assets/icons/light/delete_light.png")
        self.ctk_icon_delete = ctk.CTkImage(
                    light_image=self.icon_delete_light, 
                    dark_image=self.icon_delete_dark
                            )
        self.delete_button = ctk.CTkButton(
            self, 
            image=self.ctk_icon_delete, 
            text="", 
            command = self.handle_delete_click, 
            width=10,
            height=40, 
            fg_color="transparent")
        self.delete_button.grid(row=0, column=1, sticky = "ne", padx=10, pady=10)
        self.icon_edit_dark = Image.open("assets/icons/dark/edit_dark.png")
        self.icon_edit_light = Image.open("assets/icons/light/edit_light.png")
        self.ctk_icon_edit = ctk.CTkImage(
            light_image=self.icon_edit_light, 
            dark_image=self.icon_edit_dark
                    )
        self.modify_button = ctk.CTkButton(
            self, 
            image=self.ctk_icon_edit, 
            text="Modify", 
            command=self.handle_modify_click, 
            anchor="w", 
            width=95, 
            height=35
            )
        self.modify_button.grid(row=2, column=1, sticky = "se", padx=10, pady=10)
    def handle_delete_click(self):
        """
            Description:
                Handler that is run when clicking the delete button
    
                Notifies the GUI, to destroy the task card, 
                which notifies the backend to remove the attached task from the storage
        """
        if self.on_delete_callback:
            self.on_delete_callback(self.task_obj)
    def handle_modify_click(self):
        """
        Description:
            Handler that is run when clicking the modify button

            Signals to the GUI to launch the modification popup,
            then collects the information provided after it is finished        
        """
        if self.on_modify_callback:
            self.on_modify_callback(self.task_obj)
