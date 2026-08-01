import json
from datetime import datetime
import os
from backend import Task
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
    def add_task(self, name, tags, due_date, factor_duration, factor_urgency, ambition, description):
        """
        Description:
            Creates and adds a new task to the collection of tasks
        """
        max_attempts = 5
        for _ in range(max_attempts):
            new_task = Task(name, tags, due_date, factor_duration, factor_urgency, ambition, description)
            task_id = new_task.get_task_id()
            if task_id not in self._tasks:
                self._tasks[task_id] = new_task
                return task_id
        raise RuntimeError(f"Error: Failed to generate unique task ID after {max_attempts} attempts")

        

    def remove_task(self, task):
        """
        Description:
            Removes an existing task from the collection of tasks
        """
        if not isinstance(task, Task):
            raise TypeError(f"Error: Attempted to remove {type(task).__name__} instead of a task")
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
    #File Actions
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
                    raise ValueError (f"Data corruption detected! Key does not match task ID")
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