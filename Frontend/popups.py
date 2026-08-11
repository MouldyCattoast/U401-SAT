import customtkinter as ctk

class TaskPopup(ctk.CTkToplevel):
    def __init__(self, master):
    
        super().__init__(master)
        self.title("Add Task")
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Name", width=120)
        self.name_entry.pack(padx=20, pady=10)
        self.date_entry = ctk.CTkEntry(self, placeholder_text="Date: YYYY-MM-DD", width=180)
        self.date_entry.pack(padx= 20, pady=10)
        self.desc_textbox = ctk.CTkTextbox(
            self, 
            width=500, 
            height=300
            )
        self.desc_textbox._font = ctk.CTkFont() 
        self.desc_textbox.pack(padx=20, pady=10)
        self.desc_textbox.insert("1.0", "Enter description here.")
        self.save_button = ctk.CTkButton(self, text = "save", command = lambda: print("Saving..."))
        self.save_button.pack(padx=20, pady=10)
        self.grab_set()