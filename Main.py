import customtkinter
import json
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
    def __init__(self, task_id, name, tags_list, start_time, due_date, duration, factor_urgency, factor_ambition, status, description):
        pass
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
    def __init__(self, equilibrium_score, current_factor_ratings, target_goals, historical_data_log):
        pass
class Focus_Session():
    def __init__(self, target_task_id, target_duration, total_elapsed_time, legitimate_pause_duration, distraction_pause_duration, session_outcome):
        pass
class Task_Manager():
    def __init__(self, active_tasks, procrastinated_tasks, completed_tasks):
        pass