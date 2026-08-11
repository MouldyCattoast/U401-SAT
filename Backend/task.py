import uuid
from datetime import datetime


class Task():
    """Represents the template for what defines a task, all of the details of a task

    Attributes:
        Class Attributes:
            VALID_STATUSES (lst): The list of accepted values for status
        Instance Attributes:
            name (str): A descriptive identifier for the task used by the user(NOT USED BY THE PROGRAM TO INDENTIFY TASKS)
            duration (int): The total expected time in minutes the task will take
            tags (list): The list of tags associated with the task
            factor_urgency (int) 
            and factor_ambition (int): These are two of the "factors" the system uses to calculate the equilibrium score.
                They are about how important a task is, and how ambitious the task being undertaken is respectively.
                They accept values on a fixed integer scale from 1-10.
                These will be used to determine weighting for the equillibrium algorithm
            status (str): Variable determining whether the task is active, completed, or has been procrastinated
    """
    VALID_STATUSES = ["active", "completed", "procrastinated"]
    def __init__(self, name, due_date=None, duration=None, tags=None, factor_urgency=None, factor_ambition=None, desc=None, task_id = None, status = "active"):
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
        for tag in (tags or []):
            self.add_tag(tag)
        
        self.name = str(name)
        self.update_due_date(due_date)
        self.update_duration(duration)
        self.update_factor_urgency(factor_urgency)
        self.update_factor_ambition(factor_ambition)
        self.desc = str(desc)
        self.update_status(status)
       

    #Accessor Methods
    
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
            target_tag = target_tag.strip().lower()
        if target_tag in self._tags:
            self._tags.remove(target_tag)

    def update_duration(self, new_duration):
        """
        Description:

            Updates the value representing the total expected duration a task shall take in minutes.
        
        Justifications:
            - Duration is recorded in minutes, as this requires less computational work, and it only requires a single conversion by the system before entering data, which is much ore tidy.

        """
        if new_duration is None or new_duration =="":
            self._duration= None
            return
        if not isinstance(new_duration, int):
            raise TypeError(f"Error: Value inputted is not an integer. Data Recieved: {new_duration}")


        if new_duration <= 0:
            raise ValueError(f"Error: Value inputted must be a non-zero integer, you inputted: {type(new_duration).__name__}")
        else:
            self._duration = new_duration
    def update_due_date(self, new_due_date):
        """
        Description:
            Updates the value representing the date a task is due in the format: YYYY-MM-DD
        Justifications:
            - Uses Top Down YYYY-MM-DD to sort by the largest portion first


        """
        if not new_due_date:
            self._due_date = None
            return
        if not isinstance(new_due_date, str):
            raise TypeError(f"Error: Input Invalid. Please use a string following YYYY-MM-DD format, you inputted: {type(new_due_date).__name__}")
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
        if new_val is None:
            self._factor_urgency=0
            return
        if not isinstance(new_val, int):
            raise TypeError(f"Error: Value inputted is not an integer. Data Recieved: {type(new_val).__name__}")
        
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
        if new_val is None:
            self._factor_ambition = 0
            return
        if not isinstance(new_val, int):
            raise TypeError(f"Error: Value inputted is not an integer. Data Recieved: {type(new_val).__name__}")
        
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
            raise TypeError(f"Error: Value is not a string, you inputted{type(new_status).__name__}")
        if new_status not in self.VALID_STATUSES:
            raise ValueError(f"Error: Value not in list of valid status options, please use on of the following: 'active', 'procrastinated,'completed', You Inputted: {new_status}")
        self._status = new_status
#Utility
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
        task_dict = {
                    "task_id": self._task_id,
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
