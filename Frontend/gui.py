import customtkinter as ctk
import tkinter as tk
from backend import Task
from backend import TaskManager
from PIL import Image
from .components import TaskCard
from .popups import TaskPopup

class AephaseApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.ThemeManager.load_theme("frontend/aephase_theme.json")
        ctk.set_default_color_theme("frontend/aephase_theme.json")
        ctk.set_appearance_mode("dark")
        self.title("Aephase")
        self.geometry("1000x600")
        self.iconbitmap("assets/aephase_logo.png") 
        self.create_primary_view()
        self.create_sidebar()
        self.create_pages()
        
    def create_primary_view(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)  
        self.main_frame=ctk.CTkFrame(self, fg_color="#1A1A2E")
        self.main_frame.grid(row=0, column=1, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1) 
                
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
            size=(120,120)
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
    def create_pages(self):
        self.create_dashboard_page()
        self.create_profile_page()
        self.create_tasks_page()
        self.create_routines_page()
        self.create_recovery_page()
        self.create_focus_page()
        self.create_recollection_page()
        self.create_settings_page()
        self.hide_all_pages()
        self.show_dashboard()
    def hide_all_pages(self):
        self.dashboard_frame.grid_remove()
        self.profile_frame.grid_remove()
        self.tasks_frame.grid_remove()
        self.routines_frame.grid_remove()
        self.recovery_frame.grid_remove()
        self.focus_frame.grid_remove()
        self.recollection_frame.grid_remove()
        self.settings_frame.grid_remove()

    def create_dashboard_page(self):
        self.dashboard_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(
            self.dashboard_frame, 
            text="Dashboard (Work In Progress)", 
            font=ctk.CTkFont(
                size=24, 
                weight="bold"
                )
            ).pack()
    def create_profile_page(self):
        self.profile_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.profile_frame.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(
            self.profile_frame, 
            text="Profile (Work In Progress)", 
            font=ctk.CTkFont(
                size=24, 
                weight="bold"
                )
            ).pack()
    def create_tasks_page(self):
        self.tasks_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.tasks_frame.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(
            self.tasks_frame, 
            text="Tasks (Work In Progress)", 
            font=ctk.CTkFont(
                family="Poppins",
                size=30, 
                weight="bold"
                )
            ).pack()
        self.add_task_button = ctk.CTkButton(
            self.tasks_frame, 
            text = "+ Add Task",
            width=200,
            height=40,
            font=ctk.CTkFont(
                family="Poppins",
                size=20,
                weight="bold",
                ),
            command=lambda: TaskPopup(self)
            )
        self.add_task_button.pack(pady=10)
        self.tasks_scrollable_frame = ctk.CTkScrollableFrame(self.tasks_frame, fg_color="transparent")
        self.tasks_scrollable_frame.pack( padx=5, pady=5, fill="both", expand=True)
        self.tasks_scrollable_frame.grid_columnconfigure(0, weight=1)
        dummy_task = Task("meow" ,"changes","2025-11-22", 450, 3, 5, "nothing")
        dummy_card= TaskCard(parent_frame=self.tasks_scrollable_frame, task_obj=dummy_task)
        dummy_card.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
        dummy_card.grid_columnconfigure(0, weight=1)
    def create_recovery_page(self):
        self.recovery_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.recovery_frame.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(
            self.recovery_frame, 
            text="Recovery (Work In Progress)", 
            font=ctk.CTkFont(
                size=24, 
                weight="bold"
                )
            ).pack()
    def create_routines_page(self):
        self.routines_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.routines_frame.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(
            self.routines_frame, 
            text="Routines (Work In Progress)", 
            font=ctk.CTkFont(
                size=24, 
                weight="bold"
                )
            ).pack()
    def create_focus_page(self):
        self.focus_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.focus_frame.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(
            self.focus_frame, 
            text="Focus (Work In Progress)", 
            font=ctk.CTkFont(
                size=24, 
                weight="bold"
                )
            ).pack()
    def create_recollection_page(self):
            self.recollection_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
            self.recollection_frame.grid(row=0, column=0, sticky="nsew")
            ctk.CTkLabel(
                self.recollection_frame, 
                text="Recollection (Work In Progress)", 
                font=ctk.CTkFont(
                    size=24, 
                    weight="bold"
                    ),
                ).pack()
    def create_settings_page(self):
        self.settings_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.settings_frame.grid(row=0, column=0, sticky="nsew")
        ctk.CTkLabel(
            self.settings_frame, 
            text="Settings (Work In Progress)", 
            font=ctk.CTkFont(
                size=24, 
                weight="bold"
                ),
            ).pack()
        

    def show_dashboard(self):
        self.hide_all_pages()
        self.reset_button_colours()
        self.dashboard_frame.grid(row=0, column=0, sticky="nsew")
    def show_profile(self):
        self.hide_all_pages()
        self.reset_button_colours()
        self.btn_profile.configure(fg_color="#5e5a96")
        self.profile_frame.grid(row=0, column=0, sticky="nsew")
    def show_tasks(self):
        self.hide_all_pages()
        self.reset_button_colours()
        self.btn_tasks.configure(fg_color="#5e5a96")
        self.tasks_frame.grid(row=0, column=0, sticky="nsew")
    def show_routines(self):
        self.hide_all_pages()
        self.reset_button_colours()
        self.btn_routines.configure(fg_color="#5e5a96")
        self.routines_frame.grid(row=0, column=0, sticky="nsew")


    def show_recovery(self):
        self.hide_all_pages()
        self.reset_button_colours()
        self.btn_recovery.configure(fg_color="#5e5a96")
        self.recovery_frame.grid(row=0, column=0, sticky="nsew")
    def show_focus(self):
        self.hide_all_pages()
        self.reset_button_colours()
        self.btn_focus.configure(fg_color="#5e5a96")
        self.focus_frame.grid(row=0, column=0, sticky="nsew")
    def show_recollection(self):
        self.hide_all_pages()
        self.reset_button_colours()
        self.btn_recollection.configure(fg_color="#5e5a96")
        self.recollection_frame.grid(row=0, column=0, sticky="nsew")
    def show_settings(self):
        self.hide_all_pages()
        self.reset_button_colours()
        self.btn_settings.configure(fg_color="#5e5a96")
        self.settings_frame.grid(row=0, column=0, sticky="nsew")
    def reset_button_colours(self):
        self.btn_profile.configure(fg_color="#8A84E0")
        self.btn_tasks.configure(fg_color="#8A84E0")
        self.btn_routines.configure(fg_color="#8A84E0")
        self.btn_recovery.configure(fg_color="#8A84E0")
        self.btn_focus.configure(fg_color="#8A84E0")
        self.btn_recollection.configure(fg_color="#8A84E0")
        self.btn_settings.configure(fg_color="#8A84E0")
        

if __name__ == "__main__":
    app = AephaseApp()
    app.mainloop()
    
       