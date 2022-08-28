from django.shortcuts import render
from habit_tracker.utils import is_ajax
from habit_tracker.views.habits_view_data_extractor import HabitsViewDataExtractor


def index(request):
    return render(request, "habit_tracker/index_page.html")


def habits(request):
    if request.method == "GET":
        data_extractor = HabitsViewDataExtractor(request.user.id)
        context = {
            "column_names": data_extractor.columns,
            "rows": data_extractor.get_rows_for_table(),
        }
        return render(request, "habit_tracker/habits.html", context=context)


def update_habit(request):
    if is_ajax(request):
        habit_name, habit_date = HabitsViewDataExtractor(request.user.id).get_habit_name_and_date_from_request_body(
            request.body
        )
        print(habit_name, habit_date)
