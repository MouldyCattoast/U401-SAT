import customtkinter as ctk
from datetime import datetime

class TaskPopup(ctk.CTkToplevel):
    def __init__(self, master, on_save_callback):
    
        super().__init__(master)
        self.title("Add Task")
        self.on_save_callback=on_save_callback
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

    def handle_save_click(self):
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
