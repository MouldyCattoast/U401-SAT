# ==============================================================================
# @file:        Main.py
# @author:      mouldycattoast
# ==============================================================================
"""
This is the main file, which activates the Graphical User Interface
"""

import customtkinter
import json
import uuid
from datetime import datetime
import os
from backend import Task
from backend import TaskManager
from frontend.gui import AephaseApp

THEMES = {
    "dark": {
        "background": "#1A1A2E",
        "text": "#F0F4F8",
        "cards": "#232946",
        "buttons": "#8A84E0",
        "guidance": "#DFA59A",
        "success": "#7DD3C0"
    },
    "light": {
        "background": "#D6DDF1",
        "text": "#1E293B",
        "cards": "#F5F5FF",
        "buttons": "#6B64C9",
        "guidance": "#B87D6E",
        "success": "#4A9B94"
    }
}



if __name__ == "__main__":
    AephaseApp().mainloop()
