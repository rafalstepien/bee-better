from habit_tracker.views.habits_view_data_extractor import HabitsViewDataExtractor
from freezegun import freeze_time


@freeze_time("2022-08-28")
def test_extractor_initializes_correctly(mocker, example_list_of_habits):
    habit_objects_mock = mocker.patch(
        "habit_tracker.models.Habit.objects.filter",
        return_value=example_list_of_habits
    )

    extractor = HabitsViewDataExtractor(1)

    assert extractor.columns == ['Habit name', '22/08/2022', '23/08/2022', '24/08/2022', '25/08/2022', '26/08/2022', '27/08/2022', '28/08/2022', '29/08/2022']
    assert len(extractor.habits) == 3


def test_get_rows_for_table():
    pass


def test_get_all_habits_name():
    pass


def test_get_habit_data_from_request_body():
    pass

