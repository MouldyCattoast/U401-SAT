class Routine():

    def __init__(self, name, desc, tags_list, daily_status, recurrence_pattern):
       ...
class FixedRoutine():
    def __init__(self, start_time, end_time):
        ...
class FlexibleRoutine(Routine):
    def __init__(self, min_duration, progress, last_reset_date):
        ...