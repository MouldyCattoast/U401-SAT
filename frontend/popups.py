# ==============================================================================
# @file:        popups.py
# @author:      mouldycattoast
# ==============================================================================
"""
This module provides all of the GUI popup windows that are used for the application
"""

import customtkinter as ctk
from datetime import datetime

class TaskPopup(ctk.CTkToplevel):
    """
        Popup which displays and allows the user to edit all the user determined attributes of a specific Task
    
        Attributes:
            Instance Attributes:
                master: Window the app is launched from
                on_save_callback: Callback used by GUI to record and save information from the popup
                task_obj: Task intended to be modified (if modifying a task)
    """
    def __init__(self, master, on_save_callback, task_obj=None):
        super().__init__(master)
        
        self.task_obj=task_obj
        self.on_save_callback=on_save_callback
        self.title("Add Task")
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Name", width=120)
        self.name_entry.pack(padx=20, pady=10)
        self.due_date_entry = ctk.CTkEntry(self, placeholder_text="Due Date: YYYY-MM-DD", width=180)
        self.due_date_entry.pack(padx= 20, pady=10)
        self.duration_entry = ctk.CTkEntry(self, placeholder_text="Total Exepected Duration (Minutes)", width=240)
        self.duration_entry.pack(padx=10, pady=10)
        self.desc_textbox = ctk.CTkTextbox(
            self, 
            width=500, 
            height=300
            )
        self.desc_textbox._font = ctk.CTkFont() 
        self.desc_textbox.pack(padx=20, pady=10)
        self.desc_textbox.insert("1.0", "Enter description here.")
        self.error_label = ctk.CTkLabel(self, text="",text_color="#B87D6E")
        self.error_label.pack(pady=5)
        self.save_button = ctk.CTkButton(self, text = "Save", command = lambda: self.handle_save_click())
        self.save_button.pack(padx=20, pady=10)
        
        self.grab_set()

    def set_task_data(self, task_obj):
        """
        Parameters:
            task_obj(Task): Task which the data has been obtained frm
        Description:
            Automatically prefills the popup with the associated task's information
        """
        self.title("Modify Task")
        if task_obj.name:
            self.name_entry.insert(0, str(task_obj.name))
        if task_obj.get_due_date():
            self.due_date_entry.insert(0, str(task_obj.get_due_date()))
        if task_obj.get_duration():
            self.duration_entry.insert(0, str(task_obj.get_duration()))
        if task_obj.desc:
            self.desc_textbox.delete("1.0", "end")
            self.desc_textbox.insert("1.0", str(task_obj.desc))

    def handle_save_click(self):
        """
        Description:
            Handler that is run when clicking the save button

            Collects the the inputs of all the fields,
            Checks whether all fields have valid inputs, 
            formats the inputs, and sends them to the primary GUI window, 
            which then sends it to the backend for processing
        Justifications:
            - All inputs are stripped to remove any unnecessary spaces
            - Date must be in YYYY-MM-DD format to comply with the backend processing            
        """
        self.error_label.configure(text="")
        name = self.name_entry.get().strip()
        due_date = self.due_date_entry.get().strip()
        duration = self.duration_entry.get().strip()
        desc = self.desc_textbox.get("1.0", "end-1c")
        if not name:
            self.error_label.configure(text="Error: Task Name is required")
            return
        
        if duration:
            try:
                duration = int(duration)
            except (TypeError, ValueError):
                self.error_label.configure(
                    text=f"Error: Duration must be a whole number"
                )
                return
            if duration<=0:
                self.error_label.configure(
                    text=f"Error: Duration must be greater than 0"
                )
                return
        else:
            duration = None
        if due_date:
            try:
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                self.error_label.configure(text=f"Error Date must be in format: YYYY-MM-DD")
                return
        if not desc:
            desc = None
        if self.on_save_callback:
            self.on_save_callback(name=name,due_date=due_date,duration=duration, desc=desc)
        self.destroy()


class ConfirmationPopup(ctk.CTkToplevel):

    """
        Popup which appears to allow users to confirm their action
        Attributes:
            master: Window in which the popup was launched from
            message: Message being displayed by the popup
            on_confirm_callback: Callback used to register the option which the user has selected
            title: Window header title
            
    """
    def __init__(self, master, message, on_confirm_callback, title="Confirm Action"):
        super().__init__(master)
        self.title(title)
        
        self.on_confirm_callback = on_confirm_callback
        self.grab_set()

        self.message_label = ctk.CTkLabel(
            self, 
            text=message, 
            wraplength=300, 
            font=ctk.CTkFont(
                "Inter",
                20,
                "bold"
            )
                                          )
        self.message_label.pack(padx=20, pady=20)

        buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        buttons_frame.pack(side="bottom", fill="x", padx=20, pady=20)

        self.cancel_button = ctk.CTkButton(
            buttons_frame,
            text="Cancel",
            width=100,
            fg_color="gray",
            hover_color="#555555",
            command=self.destroy
        )
        self.cancel_button.pack(side="left")

        self.confirm_button = ctk.CTkButton(
            buttons_frame, 
            text="Confirm", 
            width=100, 
            fg_color="#B87D6E", 
            hover_color="#965D50",
            command=self.handle_confirm_click
        )
        self.confirm_button.pack(side="right")

    def handle_confirm_click(self):
        """
        Description:
            Handler that is run when clicking the confirm button

            Sends a callback, which allows the item which launched it to continue with its intended task     
        """
        if self.on_confirm_callback:
            self.on_confirm_callback()
        self.destroy()