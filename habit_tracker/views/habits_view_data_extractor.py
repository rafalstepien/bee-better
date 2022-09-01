import datetime
from typing import List

from habit_tracker.common import _date_from_slash_to_dash
from habit_tracker.models import Habit, HabitTrack, ParsedAJAXRequestData, RawAJAXRequestData


class HabitsViewDataExtractor:
    """
    Class responsible for querying the database and mining the data needed for main habit table.
    """

    NUMBER_OF_DAYS_TO_DISPLAY_BEFORE = 7
    NUMBER_OF_DAYS_TO_DISPLAY_AFTER = 1
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

    def get_habit_data_from_request_body(self, request_body: bytes) -> ParsedAJAXRequestData:
        request_data = self._extract_request_data(request_body)
        row_names = self.get_all_habit_names_for_user()
        return ParsedAJAXRequestData(
            name=row_names[request_data.row_id],
            date=_date_from_slash_to_dash(self.columns[request_data.column_id]),
            value=request_data.habit_value,
        )

    @staticmethod
    def _extract_request_data(request_body: bytes) -> RawAJAXRequestData:
        cell_identifier, habit_value = HabitsViewDataExtractor._handle_request_split(request_body)
        row_id, column_id = cell_identifier.split("=")[1].split("-")
        habit_value = HabitsViewDataExtractor._parse_habit_value(habit_value)
        return RawAJAXRequestData(row_id=int(row_id) - 1, column_id=int(column_id) - 1, habit_value=habit_value)

    @staticmethod
    def _handle_request_split(request_body: bytes):
        request_body_decoded = request_body.decode("utf-8")
        if "&" not in request_body_decoded:
            cell_identifier = request_body_decoded
            habit_value = ""
        else:
            cell_identifier, habit_value = request_body_decoded.split("&")

        return cell_identifier, habit_value

    @staticmethod
    def _parse_habit_value(habit_value):
        if "=" in habit_value:
            return True if habit_value.split("=")[1] == "True" else False
        else:
            return False

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
        self.columns = ["", "Habit name"] + dates_before_today + dates_after_today

    def _get_one_row_for_table(self, habit: Habit):
        """
        Get single row for habit table. One row contains habit name + boolean values for given range of dates.
        Here we call this range "track".
        """
        return ["", habit.habit_name, *self._get_track_for_habit(habit)]

    def _get_track_for_habit(self, habit: Habit) -> List:
        """
        Gets history track for given habit.
        """
        track = []
        for day in self.columns[2:]:
            day_in_datetime_format = datetime.datetime.strptime(day, self.DATETIME_FORMAT)
            track_for_given_day = HabitTrack.objects.filter(habit__id=habit.id, habit_date=day_in_datetime_format)
            try:
                track.append(track_for_given_day[0].habit_done)
            except IndexError:
                track.append("")
        return track
