import customtkinter
import json
import uuid
from datetime import datetime
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
factors_dict = {}

class Task():
    VALID_STATUSES = ["active", "completed", "procrastinated"]
    def __init__(self, name, tags_list, due_date, duration, factor_urgency, factor_ambition, description):
        self._task_id = str(uuid.uuid4())
        self.name = name
        self.tags_list = tags_list
        self._due_date = due_date
        self._duration = duration #Total expected duration required for the task
        self._factor_urgency = factor_urgency
        self._factor_ambition = factor_ambition
        self.description = description
        self._status = "active"


    def conv_to_dict(self):
        task_dict = {"task_id": self._task_id,
                     "name": self.name,
                     "tags_list": self.tags_list,
                     "due_date": self._due_date,
                     "duration": self._duration,
                     "factor_urgency": self._factor_urgency,
                     "factor_ambition": self._factor_ambition,
                     "description": self.description,
                     "status": self._status,
                     }
        return task_dict
    def update_factor_urgency(self, new_val):
        if not isinstance(new_val, int):
            print(f"Error: Value inputted is not an integer. Data Recieved: {new_val}")
            return
        
        if new_val>10:
            self._factor_urgency = 10
        elif new_val<1:
            self._factor_urgency = 1
        else:
            self._factor_urgency = new_val

    def update_factor_ambition(self, new_val):
            if not isinstance(new_val, int):
                print(f"Error: Value inputted is not an integer. Data Recieved: {new_val}")
                return
            
            if new_val>10:
                self._factor_ambition = 10
            elif new_val<1:
                self._factor_ambition = 1
            else:
                self._factor_ambition = new_val

    def update_duration(self, new_val):
        if not isinstance(new_val, int):
            print(f"Error: Value inputted is not an integer. Data Recieved{new_val}")
            return

        if new_val <= 0:
            print(f"Error: Value inputted must be a non-zero integer. Data Recieved{new_val}")
            return
        else:
            self._duration = new_val
    def update_due_date(self, new_val):
        if not isinstance(new_val, str):
            print(f"Error: Input Invalid. Please use a string following YYYY-MM-DD format, you inputted: {new_val}")
            return
        try:
            datetime.strptime(new_val, "%Y-%m-%d")
            self._due_date = new_val
        except ValueError:
            print(f"Error: Date format invalid. Please use YYYY-MM-DD, you inputted: {new_val}")
    def update_status(self, new_val):
        if new_val not in self.VALID_STATUSES:
            print(f"Error: Value not in list of valid status options, please use on of the following: 'active', 'procrastinated,'completed', You Inputted: {new_val}")
            return
        self._status = new_val



        
        
class Routine():
    def __init__(self, name, desc, tags_list, daily_status, recurrence_pattern, description):
        pass

class Fixed_Routine(Routine):
    def __init__(self, start_time, end_time):
        pass
class Flexible_Routine(Routine):
    def __init__(self, min_duration, progress, last_reset_date):
        pass
class User_Profile():
    def __init__(self, equilibrium_score, current_factor_ratings, target_goals, historical_data_log, decay_severity):
        pass
class Focus_Session():
    def __init__(self, target_task_id, target_duration, total_elapsed_time, legitimate_pause_duration, distraction_pause_duration, session_outcome):
        pass
class Task_Manager():
    def __init__(self, active_tasks, procrastinated_tasks, completed_tasks):
        pass

task_a = Task("lalala", ["homework", "life"], "", 55, 5, 4, "fffff")
task_a.update_status()
print(task_a.conv_to_dict())
