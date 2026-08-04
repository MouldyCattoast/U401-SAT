import customtkinter as ctk
import tkinter as tk
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
        self.create_sidebar()

    def create_sidebar(self):

        #Sidebar Setup
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.scrollable_sidebar_region = ctk.CTkScrollableFrame(
            self.sidebar, 
            width=200, 
            corner_radius=0, 
            fg_color= "transparent"
            )
        self.scrollable_sidebar_region.grid(row=1, column=0, sticky="nsew", padx=5)
        self.sidebar.grid_rowconfigure(1, weight=1)

        #Dashboard/Logo Button
        self.logo_image= Image.open("assets/aephase_logo.png")
        self.ctk_logo = ctk.CTkImage(
            light_image=self.logo_image, 
            dark_image=self.logo_image, 
            size=(100,100)
            )
        self.logo_button = ctk.CTkButton(
            self.sidebar, 
            image=self.ctk_logo, 
            text="", 
            fg_color="transparent", 
            hover_color="#232946", 
            command=self.show_dashboard
            )
        self.logo_button.grid(row=0, column=0, padx=20,pady=20)
        self.main_frame=ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew")

        #Profile Button
        self.icon_profile_dark = Image.open("assets/icons/dark/profile_dark.png")
        self.icon_profile_light = Image.open("assets/icons/light/profile_light.png")
        self.ctk_icon_profile = ctk.CTkImage(
            light_image=self.icon_profile_light, 
            dark_image=self.icon_profile_dark
            )
        self.btn_profile = ctk.CTkButton(
            self.scrollable_sidebar_region,
            image=self.ctk_icon_profile, 
            text="Profile", 
            command=self.show_profile,
            anchor="w"
            )
        self.btn_profile.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        #Tasks Button
        self.icon_tasks_dark = Image.open("assets/icons/dark/tasks_dark.png")
        self.icon_tasks_light = Image.open("assets/icons/light/tasks_light.png")
        self.ctk_icon_tasks = ctk.CTkImage(
            light_image=self.icon_tasks_light, 
            dark_image=self.icon_tasks_dark
            )
        self.btn_tasks = ctk.CTkButton(
            self.scrollable_sidebar_region, 
            image=self.ctk_icon_tasks,
            text="Tasks", 
            command=self.show_tasks,
            anchor="w"
            )
        self.btn_tasks.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        #Routine Button
        self.icon_routine_dark = Image.open("assets/icons/dark/routines_dark.png")
        self.icon_routine_light = Image.open("assets/icons/light/routines_light.png")
        self.ctk_icon_routine = ctk.CTkImage(
            light_image=self.icon_routine_light, 
            dark_image=self.icon_routine_dark
            )
        self.btn_routines = ctk.CTkButton(
            self.scrollable_sidebar_region,
            image=self.ctk_icon_routine,
            text="Routines", 
            command=self.show_routines,
            anchor="w"
            )
        self.btn_routines.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        #Recovery Button
        self.icon_recovery_dark = Image.open("assets/icons/dark/recovery_dark.png")
        self.icon_recovery_light = Image.open("assets/icons/light/recovery_light.png")
        self.ctk_icon_recovery = ctk.CTkImage(
            light_image=self.icon_recovery_light, 
            dark_image=self.icon_recovery_dark
            )
        self.btn_recovery = ctk.CTkButton(
            self.scrollable_sidebar_region, 
            image=self.ctk_icon_recovery,
            text="Recovery", 
            command=self.show_recovery,
            anchor="w"
            )
        self.btn_recovery.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        #Focus Button
        self.icon_focus_dark = Image.open("assets/icons/dark/focus_dark.png")
        self.icon_focus_light = Image.open("assets/icons/light/focus_light.png")
        self.ctk_icon_focus = ctk.CTkImage(
            light_image=self.icon_focus_light, 
            dark_image=self.icon_focus_dark
            )
        self.btn_focus = ctk.CTkButton(
            self.scrollable_sidebar_region, 
            image=self.ctk_icon_focus,
            text="Focus", 
            command=self.show_focus,
            anchor="w"
            )
        self.btn_focus.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        #Recollection Button
        self.icon_recollection_dark = Image.open("assets/icons/dark/recollection_dark.png")
        self.icon_recollection_light = Image.open("assets/icons/light/recollection_light.png")
        self.ctk_icon_recollection = ctk.CTkImage(
            light_image=self.icon_recollection_light, 
            dark_image=self.icon_recollection_dark
            )
        self.btn_recollection = ctk.CTkButton(
            self.scrollable_sidebar_region,
            image=self.ctk_icon_recollection, 
            text="Recollection", 
            command=self.show_recollection,
            anchor="w"
            )
        self.btn_recollection.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        #Settings Button
        self.icon_settings_dark = Image.open("assets/icons/dark/settings_dark.png")
        self.icon_settings_light = Image.open("assets/icons/light/settings_light.png")
        self.ctk_icon_settings = ctk.CTkImage(
            light_image=self.icon_settings_light, 
            dark_image=self.icon_settings_dark
            )
        self.btn_settings = ctk.CTkButton(
            self.scrollable_sidebar_region,
            image=self.ctk_icon_settings, 
            text="Settings", 
            command=self.show_settings,
            anchor="w"
            )
        self.btn_settings.grid(row=6, column=0, padx=20, pady=10, sticky="ew")

    def show_dashboard(self):
        pass
    def show_profile(self):
        pass
    def show_tasks(self):
        pass
    def show_recovery(self):
        pass
    def show_routines(self):
        pass
    def show_focus(self):
        pass
    def show_recollection(self):
        pass
    def show_settings(self):
        pass

if __name__ == "__main__":
    app = AephaseApp()
    app.mainloop()
    
       