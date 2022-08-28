import datetime
from typing import List, Tuple

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
        self.habits = Habit.objects.filter(user__id=self.user_id)

        self._get_habit_column_names()

    def get_rows_for_table(self) -> List:
        """
        Get the rows for main habit table.
        """
        return [self._get_one_row_for_table(habit) for habit in self.habits]

    def get_all_habit_names_for_user(self) -> List[str]:
        return [habit.habit_name for habit in self.habits]

    def get_habit_name_and_date_from_request_body(self, request_body: bytes) -> Tuple[str, str]:
        row_id, column_id = self._extract_row_and_column_id(request_body)
        column_names = self.columns
        row_names = self.get_all_habit_names_for_user()
        return row_names[row_id], column_names[column_id]

    @staticmethod
    def _extract_row_and_column_id(request_body: bytes) -> List[int]:
        return [int(id_number) - 1 for id_number in request_body.decode("utf-8").split("-")]

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
