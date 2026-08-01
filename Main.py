import customtkinter
import json
import uuid
from datetime import datetime
import os
from Backend import Task
from Backend import TaskManager

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




class FocusSession():
    def __init__(self, target_task_id, target_duration, total_elapsed_time, legitimate_pause_duration, distraction_pause_duration, session_outcome):
        pass

try:
    task_a = Task("lalala", ["catty fat", "fatty cat   ", "MEloN"], "2025-12-31", 55, 12, 4, "fffff")
    print(task_a.conv_to_dict())
except (TypeError, ValueError) as error:
    print(f"Task creation blocked: {error}")
