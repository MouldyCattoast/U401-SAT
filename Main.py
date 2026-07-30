import customtkinter
import json
import uuid
from datetime import datetime
import os
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
        Class Attributes:
            VALID_STATUSES (lst): The list of accepted values for status
        Instance Attributes:
            name (str): A descriptive identifier for the task used by the user(NOT USED BY THE PROGRAM TO INDENTIFY TASKS)
            tags (list): The list of tags associated with the task
            duration (int): The total expected time in minutes the task will take
            factor_urgency (int) 
            and factor_ambition (int): These are two of the "factors" the system uses to calculate the equilibrium score.
                They are about how important a task is, and how ambitious the task being undertaken is respectively.
                They accept values on a fixed integer scale from 1-10.
                These will be used to determine weighting for the equillibrium algorithm
            status (str): Variable determining whether the task is active, completed, or has been procrastinated
    """
    VALID_STATUSES = ["active", "completed", "procrastinated"]
    def __init__(self, name, tags, due_date, duration, factor_urgency, factor_ambition, desc, task_id = None, status = "active"):
        """
        Jusifications:
            - init uses setters to define most attributes so that they can be validated
            - task_id uses UUID so that
        """
        if task_id:
            self._task_id = task_id
        else:
            self._task_id = str(uuid.uuid4())

        self._tags = []
        for tag in tags:
            self.add_tag(tag)
        
        self.name = str(name)
        self.update_due_date(due_date)
        self.update_duration(duration)
        self.update_factor_urgency(factor_urgency)
        self.update_factor_ambition(factor_ambition)
        self.desc = str(desc)
        self.update_status(status)
       

    #Accessor Methods
    def conv_to_dict(self):
        """
        Description:
            Converts the object into dictionary format, where each attribute is a key.
            This is for later use regarding data storage
        Justifications:
            - Dictionary used to store data rather than lists as dictionaries better match the nature of objects being that they have descriptive attributes.
            Additionally, 
            Using a list instead would make code much less readable and prone to errors
            - UUID is used for identification for tasks, as it generates a unique code.
            If something like a regular number were used to indentify tasks, say the 
        """
        task_dict = {"task_id": self._task_id,
                        "name": self.name,
                        "tags": self._tags,
                        "due_date": self._due_date,
                        "duration": self._duration,
                        "factor_urgency": self._factor_urgency,
                        "factor_ambition": self._factor_ambition,
                        "description": self.desc,
                        "status": self._status,
                        }
        return task_dict
    
    def get_task_id(self):
        """
        Description:
            Returns the task's ID
        """
        return self._task_id


    def get_tags(self):
        """
        Description:
            Returns the list of tags associated with the task
        """
        return self._tags

    def get_duration(self):
        """
        Description:
            Returns the the total expected duration of the task
        """
        return self._duration
    def get_due_date(self):
        """
        Description:
            Returns the due date of the task
        """
        return self._due_date
    
    def get_urgency_val(self):
        """
        Description:
            Returns the magnitude of the urgency factor for the task
        """
        return self._factor_urgency
    
    def get_ambition_val(self):
        """
        Description:
            Returns the magnitude of the ambition factor for the task
        """
        return self._factor_ambition
    def get_status(self):
        """
        Description:
            Returns the task's current status
        """
        return self._status


    #Mutator Methods
    def add_tag(self, new_tag):
        """
        Description:
            Adds a new tag to the list of tags associated with the task
        Justifcations:
        """
        if not isinstance(new_tag, str):
            raise TypeError(f"Error: Tags must be a string. Type Inputted: {type(new_tag)}")
        new_tag = new_tag.strip().lower()
        if new_tag in self._tags:
            raise ValueError(f"Error: Tag {new_tag} already exists for the requested task, pleas try a tag that does not yet exist for this task")
        self._tags.append(new_tag)

    def remove_tag(self, target_tag):
        """
        Description:
            Removes the specified tag from the list of tags associated with the task
        Justifications:
            Target tag is stripped and lowered to match naming convention for tags
        """
        if isinstance(target_tag, str):
            target_tag.strip().lower()
        if target_tag in self._tags:
            self._tags.remove(target_tag)

    def update_duration(self, new_duration):
        """
        Description:

            Updates the value representing the total expected duration a task shall take in minutes.
        
        Justifications:
            - Duration is recorded in minutes, as this requires less computational work, and it only requires a single conversion by the system before entering data, which is much ore tidy.

        """
        if not isinstance(new_duration, int):
            raise TypeError(f"Error: Value inputted is not an integer. Data Recieved: {type(new_duration)}")


        if new_duration <= 0:
            raise TypeError(f"Error: Value inputted must be a non-zero integer, you inputted: {type(new_duration)}")
        else:
            self._duration = new_duration
    def update_due_date(self, new_due_date):
        """
        Description:
            Updates the value representing the date a task is due in the format: YYYY-MM-DD
        Justifications:
            - Uses Top Down YYYY-MM-DD to sort by the largest portion first


        """
        if not isinstance(new_due_date, str):
            raise TypeError(f"Error: Input Invalid. Please use a string following YYYY-MM-DD format, you inputted: {new_due_date}")
        try:
            datetime.strptime(new_due_date, "%Y-%m-%d")
            self._due_date = new_due_date
        except ValueError:
            raise ValueError(f"Error: Date format invalid. Please use YYYY-MM-DD, you inputted: {new_due_date}")
    def update_factor_urgency(self, new_val):
        """
        Description:
            Updates the value of the variable representing the factor of urgency.
            Accepts integer value in the following range: 1<=n<=10
        Justifications:
            - A range of 1-10 is typical for user rated metrics as humans understand percentages well, which are written in base 10 automatically.
            - A range of 1-10 mimics this as it is similarly base 10.
            - A more specific range such as 1-100 and also floats such as 7.58 are avoided, as users will find it hard to imagine subjective ratings to such a small scale.
            - Similarly, a less specific range such as 1-5 is avoided, as it might not offer the same flexibility as a scale of 1-10.
            - As such 1-10 is a good choice for this.
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
        Description:
            Updates the value of the variable representing the factor of ambition.
            Accepts integer value in the following range: 1<=n<=10
        Justifications:
            - A range of 1-10 is typical for user rated metrics as humans understand percentages well, which are written in base 10 automatically.
            - A range of 1-10 mimics this as it is similarly base 10.
            - A more specific range such as 1-100 and also floats such as 7.58 are avoided, as users will find it hard to imagine subjective ratings to such a small scale.
            - Similarly, a less specific range such as 1-5 is avoided, as it might not offer the same flexibility as a scale of 1-10.
                As such 1-10 is a good choice for this.
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

    def update_status(self, new_status):
        """
        Description:
            Updates the status of the task, valid options include "active", "procrastinated" and "completed"
        """
        if not isinstance(new_status ,str):
            raise TypeError(f"Error: Value is not a string, you inputted{type(new_status)}")
        if new_status not in self.VALID_STATUSES:
            raise ValueError(f"Error: Value not in list of valid status options, please use on of the following: 'active', 'procrastinated,'completed', You Inputted: {new_status}")
        self._status = new_status

class Routine():

    def __init__(self, name, desc, tags_list, daily_status, recurrence_pattern):
       pass
class FixedRoutine():
    def __init__(self, start_time, end_time):
        pass
class FlexibleRoutine(Routine):
    def __init__(self, min_duration, progress, last_reset_date):
        pass
class UserProfile():
    def __init__(self, equilibrium_score, current_factor_ratings, target_goals, historical_data_log, decay_severity):
        pass
class FocusSession():
    def __init__(self, target_task_id, target_duration, total_elapsed_time, legitimate_pause_duration, distraction_pause_duration, session_outcome):
        pass

class TaskManager():
    """
    Manages the collection of tasks and routines
    Attributes:
        Instance Attributes:
            self._tasks (dict) : The collection of all stored tasks.
                Reference key for each task is their unique task ID
            self._routines (dict): The collection of all stored routines.
                Reference key for each routine is their unique ID

    """
    def __init__(self):
        self._tasks = {}
        self._routines = {}
    #Accessor Methods
    def get_task(self, task_id):
        """
        Description:
            Uses a task ID to identify and return the object assoiated with the ID
        """
        if task_id not in self._tasks:
            raise ValueError(f"Error: Target task was not found")
        return self._tasks[task_id]
        
    def get_all_tasks(self):
        """
        Description:
            Returns a list of the all of the objects stored in the dictionary "tasks"
        """
        return list(self._tasks.values())

    #Mutator Methods
    def add_task(self, task):
        """
        Description:
            Adds a new task to the collection of tasks
        """
        if not isinstance(task, Task):
            raise TypeError(f"Error: Attempted to add {type(task)} instead of a task")
        if task._task_id in self._tasks:
            raise ValueError(f"Error: Task already in list of tasks")
        self._tasks[task._task_id] = task

    def remove_task(self, task):
        """
        Description:
            Removes an existing task from the collection of tasks
        """
        if not isinstance(task, Task):
            raise TypeError(f"Error: Attempted to remove {type(task)} instead of a task")
        if task._task_id not in self._tasks:
            raise ValueError(f"Error: Target task was not found")
        self._tasks.pop(task._task_id)

    
    def duplicate_task(self, task_id):
        """
        Description:
            Creates a copy of a selected task's data and assigns the copy to a new ID
        """
        og_task = self.get_task(task_id) #shorthand for original task
        new_task = Task(og_task.name, list(og_task._tags), og_task._due_date, og_task._duration, og_task._factor_urgency, og_task._factor_ambition, og_task.desc)
        self._tasks[new_task._task_id] = new_task

    def update_task_status(self, task_id, new_status):
        """
        Description:
            Updates the task status.
            Valid Statuses include: active, procrastinated and completed
        """
        task = self.get_task(task_id)
        task.update_status(new_status)
    #Actions
    def save_tasks(self):
        tasks_to_save = {}
        for task_id, task in self._tasks.items():
            tasks_to_save[task_id] = task.conv_to_dict()
        with open("tasks.json", "w") as file:
            json.dump(tasks_to_save, file , indent=4)
    def load_tasks(self):
        if not os.path.exists("tasks.json"):
            print("No tasks were found")
            return
        with open("tasks.json", "r") as file:
            loaded_data = json.load(file)
            for task_id, task_data in loaded_data.items():
                if task_id != task_data["task_id"]:
                    raise ValueError (f"Data corruption detected! Key {task_id} does not match task ID {task_data['task_id']}")
                name = task_data["name"]
                tags = task_data["tags"]
                due_date = task_data["due_date"]
                duration = task_data["duration"]
                factor_urgency = task_data["factor_urgency"]
                factor_ambition = task_data["factor_ambition"]
                desc = task_data["description"]
                status = task_data["status"]

                new_task = Task(name, tags, due_date, duration, factor_urgency, factor_ambition, desc, task_id, status)
                self._tasks[task_id] = new_task


    
        

try:
    task_a = Task("lalala", ["catty fat", "fatty cat   ", "MEloN"], "2025-12-31", 55, 12, 4, "fffff")
    print(task_a.conv_to_dict())
except (TypeError, ValueError) as error:
    print(f"Task creation blocked: {error}")
