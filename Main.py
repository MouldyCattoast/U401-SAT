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
    """Represents the template for what defines a task, all of the details of a task

    Attributes:
        tags (lst): The list of tags associated with the task
        duration (int): The total expected time in minutes the task will take
        factor_urgency and factor_ambition (int): These are two of the "factors" the system uses to calculate the equilibrium score.
            They are about how important a task is, and how ambitious the task being undertaken is respectively.
            They accept values on a fixed integer scale from 1-10.
            These will be used to determine weighting for the equillibrium algorithm
        status (str): Variable determining whether the task is active, completed, or has been procrastinated
    """
    VALID_STATUSES = ["active", "completed", "procrastinated"] # A list of values accepted as a status
    def __init__(self, name, tags, due_date, duration, factor_urgency, factor_ambition, desc):

        self._tags = []
        for tag in tags:
            self.add_tag(tag)
        self._task_id = str(uuid.uuid4())
        self.name = str(name)
        self.update_due_date(due_date)
        self.update_duration(duration)
        self.update_factor_urgency(factor_urgency)
        self.update_factor_ambition(factor_ambition)
        self.desc = str(desc)
        self.update_status("active")

    def add_tag(self, new_tag):
        """
        Adds a new tag to the list of tags associated with the task
        """
        if not isinstance(new_tag, str):
            raise TypeError(f"Error: Tags must be a string. Type Inputted: {type(new_tag)}")
        new_tag = new_tag.strip().lower()
        if new_tag in self._tags:
            raise ValueError(f"Error: Tag {new_tag} already exists for the requested task, pleas try a tag that does not yet exist for this task")
        self._tags.append(new_tag)

    def remove_tag(self, target_tag):
        """
        Removes the specified tag from the list of tags associated with the task
        """
        if isinstance(target_tag, str):
            target_tag.strip().lower()
        if target_tag in self._tags:
            self._tags.remove(target_tag)


    def conv_to_dict(self):
        """
        Converts the object into dictionary format, where each attribute is a key.
        This is for later use regarding data storage
        """
        task_dict = {"task_id": self._task_id,
                     "name": self.name,
                     "tags_list": self._tags,
                     "due_date": self._due_date,
                     "duration": self._duration,
                     "factor_urgency": self._factor_urgency,
                     "factor_ambition": self._factor_ambition,
                     "description": self.desc,
                     "status": self._status,
                     }
        return task_dict
    
    def update_factor_urgency(self, new_val):
        """
        Updates the value of the variable representing the factor of urgency.
        Accepts integer value in the following range: 1<=n<=10
        """
        if not isinstance(new_val, int):
            raise TypeError(f"Error: Value inputted is not an integer. Data Recieved: {new_val}")
        
        if new_val>10:
            self._factor_urgency = 10
        elif new_val<1:
            self._factor_urgency = 1
        else:
            self._factor_urgency = new_val

    def update_factor_ambition(self, new_val):
            """
            Updates the value of the variable representing the factor of ambition.
            Accepts integer value in the following range: 1<=n<=10
            """
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
        """
        Updates the value representing the total expected duration a task shall take in minutes
        """
        if not isinstance(new_val, int):
            raise TypeError(f"Error: Value inputted is not an integer. Data Recieved: {type(new_val)}")


        if new_val <= 0:
            raise TypeError(f"Error: Value inputted must be a non-zero integer, you inputted: {type(new_val)}")
        else:
            self._duration = new_val
    def update_due_date(self, new_val):
        """
        Updates the value representing the date a task is due in the format: YYYY-MM-DD
        """
        if not isinstance(new_val, str):
            raise TypeError(f"Error: Input Invalid. Please use a string following YYYY-MM-DD format, you inputted: {new_val}")
        try:
            datetime.strptime(new_val, "%Y-%m-%d")
            self._due_date = new_val
        except ValueError:
            raise ValueError(f"Error: Date format invalid. Please use YYYY-MM-DD, you inputted: {new_val}")
            
    def update_status(self, new_val):
        """
        Updates the status of the task, valid options include "active", "procrastinated" and "completed"
        """
        if not isinstance(new_val ,str):
            raise TypeError(f"Error: Value is not a string, you inputted{type(new_val)}")
        if new_val not in self.VALID_STATUSES:
            raise ValueError(f"Error: Value not in list of valid status options, please use on of the following: 'active', 'procrastinated,'completed', You Inputted: {new_val}")
        self._status = new_val

class Routine():
    def __init__(self, name, desc, tags_list, daily_status, recurrence_pattern):
       pass
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
    def __init__(self):
        self._tasks = {}
        self._routines = {}
    def add_task(self, task):
        if not isinstance(task, Task):
            raise TypeError(f"Error: Attempted to add {type(task)} instead of a task")
        if task._task_id in self._tasks:
            raise ValueError(f"Error: Task already in list of tasks")
        self._tasks[task._task_id] = task
    def remove_task(self, task):
        if not isinstance(task, Task):
            raise TypeError(f"Error: Attempted to remove {type(task)} instead of a task")
        if task._task_id not in self._tasks:
            raise ValueError(f"Error: Target task was not found")
        self._tasks.pop(task._task_id)
        

try:
    task_a = Task("lalala", ["catty fat", "fatty cat   ", "MEloN"], "2025-12-31", 55, 12, 4, "fffff")
    print(task_a.conv_to_dict())
except (TypeError, ValueError) as error:
    print(f"Task creation blocked: {error}")
