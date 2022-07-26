from django.shortcuts import render
from habit_tracker.views.habits_view_data_extractor import HabitsViewDataExtractor


def index(request):
    return render(request, "habit_tracker/index_page.html")


def habits(request):
    if request.method == "POST":
        pass
    else:
        data_extractor = HabitsViewDataExtractor(request.user.id)
        context = {
            "column_names": data_extractor.columns,
            "rows": data_extractor.get_rows_for_table(),
        }
        return render(request, "habit_tracker/habits.html", context=context)
