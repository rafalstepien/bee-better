import datetime
from typing import List

from habit_tracker.models import Habit, HabitTrack


class HabitsViewDataExtractor:
    """
    Class responsible for querying the database and mining the data needed for main habit table.
    """

    NUMBER_OF_DAYS_TO_DISPLAY_BEFORE = 7
    NUMBER_OF_DAYS_TO_DISPLAY_AFTER = 7
    DATETIME_FORMAT = "%d/%m/%Y"

    def __init__(self, user_id: int):
        self.user_id = user_id
        self.columns = None

        self._get_habit_column_names()

    def _get_habit_column_names(self):
        """
        Set the correct column names for table.
        """
        today = datetime.datetime.today()
        dates_before_today = [
            (today - datetime.timedelta(days=num_days)).strftime(self.DATETIME_FORMAT)
            for num_days in range(self.NUMBER_OF_DAYS_TO_DISPLAY_BEFORE)
        ][::-1]
        dates_after_today = [
            (today + datetime.timedelta(days=num_days)).strftime(self.DATETIME_FORMAT)
            for num_days in range(1, self.NUMBER_OF_DAYS_TO_DISPLAY_AFTER)
        ]
        self.columns = ["Habit name"] + dates_before_today + dates_after_today

    def get_rows_for_table(self) -> List:
        """
        Get the rows for main habit table.
        """
        habits_for_given_user = Habit.objects.filter(user__id=self.user_id)
        return [self._get_one_row_for_table(habit) for habit in habits_for_given_user]

    def _get_one_row_for_table(self, habit: Habit):
        """
        Get single row for habit table. One row contains habit name + boolean values for given range of dates.
        Here we call this range "track".
        """
        return [habit.habit_name, *self._get_track_for_habit(habit)]

    def _get_track_for_habit(self, habit: Habit) -> List:
        """
        Gets history track for given habit.
        """
        track = []
        for day in self.columns[1:]:
            day_in_datetime_format = datetime.datetime.strptime(day, self.DATETIME_FORMAT)
            track_for_given_day = HabitTrack.objects.filter(habit__id=habit.id, habit_date=day_in_datetime_format)
            try:
                track.append(track_for_given_day[0].habit_done)
            except IndexError:
                track.append("")
        return track
