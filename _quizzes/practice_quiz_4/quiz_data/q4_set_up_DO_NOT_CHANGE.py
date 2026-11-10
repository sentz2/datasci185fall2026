# Quiz 4 set-up script.  DO NOT CHANGE.


import random
import pandas as pd

df = pd.read_csv("quiz_data/student_plus_scores.csv")
names = list(df["name"])
staminas = list(df["stamina"])

# every student's stamina, looked up by name
all_staminas = {}
for i in range(len(names)):
    all_staminas[names[i]] = int(staminas[i])

# a random club of 8 runners: this changes every time this script runs
club_names = random.sample(names, k = 8)

roster = {}
for name in club_names:
    roster[name] = all_staminas[name]


class Runner:
    """A member of the Emory Run Club."""

    def __init__(self, name, stamina):
        self.name = name
        self.stamina = stamina
        self.num_runs = 0
        self.pace_buddy = None

    def __str__(self):
        return f"{self.name} (stamina {round(self.stamina, 1)})"

    # ---------- getters ----------

    def get_name(self):
        return self.name

    def get_stamina(self):
        return self.stamina

    def get_num_runs(self):
        return self.num_runs

    def get_pace_buddy(self):
        return self.pace_buddy

    # ---------- setters ----------

    def set_stamina(self, value):
        assert 0 <= value <= 100, "stamina must be between 0 and 100"
        self.stamina = value

    def set_pace_buddy(self, other):
        """Make self and other each other's pace buddy."""
        self.pace_buddy = other
        other.pace_buddy = self

    # ---------- scoring ----------

    def run_value(self, score):
        return score
