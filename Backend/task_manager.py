# ==============================================================================
# @file:        task_manager.py
# @author:      mouldycattoast
# ==============================================================================
"""
This module provides the TaskManager class, 
which manages the entire collection of tasks while the program is running.

It has the capability to add, remove and duplicate tasks, 
but does not have the capibility to modify individual tasks

It also is responsible for writing task information to the tasks.json file so it can be stored throughout sessions
"""

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
    def __init__(self, filename="tasks.json"):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(base_dir)
        data_dir = os.path.join(project_root, "data")
        os.makedirs(data_dir, exist_ok=True)
        self._filename = os.path.join(data_dir, filename)
        self._tasks = {}
        self._routines = {}
        self.load_tasks()
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
    def add_task(
        self, 
        name=None, 
        due_date=None, 
        duration=None, 
        tags=None, 
        factor_ambition=None, 
        factor_urgency=None, 
        desc=None,
        save=True
    ):
        """
        Description:
            Creates and adds a new task to the collection of tasks
        """
        max_attempts = 5
        for _ in range(max_attempts):
            new_task = Task(
                name=name, 
                due_date=due_date, 
                duration=duration, 
                tags=tags,  
                factor_urgency=factor_urgency, 
                factor_ambition=factor_ambition, 
                desc=desc,
                )
            task_id = new_task.get_task_id()
            if task_id not in self._tasks:
                self._tasks[task_id] = new_task

                if save:
                    self.save_tasks()
                return task_id
        raise RuntimeError(f"Error: Failed to generate unique task ID after {max_attempts} attempts")

        

        

    def remove_task(self, task, save=True):
        """
        Description:
            Removes an existing task from the collection of tasks
        """
        if not isinstance(task, Task):
            raise TypeError(f"Error: Attempted to remove {type(task).__name__} instead of a task")
        if task.get_task_id() not in self._tasks:
            raise ValueError(f"Error: Target task was not found")
        self._tasks.pop(task.get_task_id())
        if save:
            self.save_tasks()

    
    def duplicate_task(self, task_id, save=True):
        """
        Description:
            Creates a copy of a selected task's data and assigns the copy to a new ID
        """
        og_task = self.get_task(task_id) #shorthand for original task
        og_tags=og_task.get_tags()
        og_tags = list(og_tags) if og_tags is not None else None
        new_task = Task(
            name=og_task.name, 
            tags=list(og_tags), 
            due_date=og_task.get_due_date(), 
            duration=og_task.get_duration(), 
            factor_urgency=og_task.get_urgency_val(), 
            factor_ambition=og_task.get_ambition_val(), 
            desc=og_task.desc
            )
        self._tasks[new_task.get_task_id()] = new_task
        if save:
            self.save_tasks()

    def update_task_status(self, task_id, new_status, save=True):
        """
        Description:
            Updates the task status.
            Valid Statuses include: active, procrastinated and completed
        """
        task = self.get_task(task_id)
        task.update_status(new_status)
        if save:
            self.save_tasks()
    #File Actions
    def save_tasks(self):
        """
        Description:
            Converts all objects of class Task into dictionaries, and writes them to tasks.json
        """
        tasks_to_save = {}
        for task_id, task in self._tasks.items():
            tasks_to_save[task_id] = task.conv_to_dict()
        with open(self._filename, "w") as file:
            json.dump(tasks_to_save, file , indent=4)

    def load_tasks(self):
        """
        Description:
            Reads tasks.json and converts all stored objects and their listed attributes into objects of class Task
        """
        if not os.path.exists(self._filename):
            print("No tasks were found")
            return
        with open(self._filename, "r") as file:
            loaded_data = json.load(file)
            for task_id, task_data in loaded_data.items():
                if task_id != task_data["task_id"]:
                    raise ValueError (f"Data corruption detected! Key does not match task ID")
                name = task_data["name"]
                due_date = task_data["due_date"]
                duration = task_data["duration"]
                tags = task_data["tags"]
                factor_urgency = task_data["factor_urgency"]
                factor_ambition = task_data["factor_ambition"]
                desc = task_data["description"]
                status = task_data["status"]

                new_task = Task(name=name, 
                                due_date=due_date, 
                                duration=duration, 
                                tags=tags, 
                                factor_urgency=factor_urgency, 
                                factor_ambition=factor_ambition, 
                                desc=desc, 
                                task_id=task_id, 
                                status=status)
                self._tasks[task_id] = new_task