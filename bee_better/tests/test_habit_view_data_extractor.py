from freezegun import freeze_time
from habit_tracker.views.habits_view_data_extractor import HabitsViewDataExtractor
from habit_tracker.models import ParsedAJAXRequestData


@freeze_time("2022-08-28")
def test_extractor_initializes_correctly(mocker, example_list_of_habits):
    mocker.patch("habit_tracker.models.Habit.objects.filter", return_value=example_list_of_habits)

    extractor = HabitsViewDataExtractor(1)

    assert extractor.columns == [
        "Habit name",
        "22/08/2022",
        "23/08/2022",
        "24/08/2022",
        "25/08/2022",
        "26/08/2022",
        "27/08/2022",
        "28/08/2022",
        "29/08/2022",
    ]
    assert len(extractor.habits) == 3


def test_get_rows_for_table(mocker, example_list_of_habits):
    mocker.patch("habit_tracker.models.Habit.objects.filter", return_value=example_list_of_habits)
    mocker.patch("habit_tracker.models.HabitTrack.objects.filter", return_value=[])

    extractor = HabitsViewDataExtractor(1)

    assert extractor.get_rows_for_table() == [
        ["habit_1", "", "", "", "", "", "", "", ""],
        ["habit_2", "", "", "", "", "", "", "", ""],
        ["habit_3", "", "", "", "", "", "", "", ""],
    ]


def test_get_all_habits_names(mocker, example_list_of_habits):
    mocker.patch("habit_tracker.models.Habit.objects.filter", return_value=example_list_of_habits)
    assert HabitsViewDataExtractor(1).get_all_habit_names_for_user() == ['habit_1', 'habit_2', 'habit_3']


def test_get_habit_data_from_request_body(mocker, example_list_of_habits):
    mocker.patch("habit_tracker.models.Habit.objects.filter", return_value=example_list_of_habits)

    data = HabitsViewDataExtractor(1).get_habit_data_from_request_body(
        bytes("element_id=2-3&habitDone=False", "utf-8")
    )

    assert data == ParsedAJAXRequestData(
        name="habit_2",
        date="2022-08-23",
        value=False
    )

