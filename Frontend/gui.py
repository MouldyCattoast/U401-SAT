import customtkinter as ctk
from backend import Task
from backend import TaskManager
from PIL import Image

class AephaseApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.ThemeManager.load_theme("frontend/aephase_theme.json")
        ctk.set_default_color_theme("frontend/aephase_theme.json")
        ctk.set_appearance_mode("dark")
        self.title("Aephase")
        self.geometry("1000x600")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.logo_image= Image.open("assets/aephase_logo.png")
        self.ctk_logo = ctk.CTkImage(light_image=self.logo_image, dark_image=self.logo_image, size=(100,100))

        self.logo_button = ctk.CTkButton(self.sidebar, image=self.ctk_logo, text="", fg_color="transparent", hover_color="#232946", command=self.show_dashboard)
        self.logo_button.grid(row=0, column=0, padx=20,pady=20)
        self.main_frame=ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.btn_profile = ctk.CTkButton(self.sidebar, text="Profile", command=self.show_profile)
        self.btn_profile.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        self.btn_tasks = ctk.CTkButton(self.sidebar, text="Tasks", command=self.show_tasks)
        self.btn_tasks.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.btn_recovery = ctk.CTkButton(self.sidebar, text="Recovery", command=self.show_recovery)
        self.btn_recovery.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.btn_routines = ctk.CTkButton(self.sidebar, text="Routines", command=self.show_routines)
        self.btn_routines.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        self.btn_focus = ctk.CTkButton(self.sidebar, text="Focus", command=self.show_focus)
        self.btn_focus.grid(row=5, column=0, padx=20, pady=10, sticky="ew")
        self.btn_settings = ctk.CTkButton(self.sidebar, text="Settings", command=self.show_settings)
        self.btn_settings.grid(row=6, column=0, padx=20, pady=10, sticky="ew")

    def show_dashboard():
        pass
    def show_profile():
        pass
    def show_tasks():
        pass
    def show_recovery():
        pass
    def show_routines():
        pass
    def show_focus():
        pass
    def show_settings():
        pass

if __name__ == "__main__":
    app = AephaseApp()
    app.mainloop()
    
       