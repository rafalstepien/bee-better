from django.shortcuts import render
from habit_tracker.common import ColorsHEX, ColorsRGB, is_ajax
from habit_tracker.models import Habit, HabitTrack
from habit_tracker.views.habits_view_data_extractor import HabitsViewDataExtractor


def index(request):
    return render(request, "habit_tracker/index_page.html")


def habits(request):
    if request.method == "GET":
        data_extractor = HabitsViewDataExtractor(request.user.id)
        context = {
            "column_names": data_extractor.columns,
            "rows": data_extractor.get_rows_for_table(),
            "colors_rgb": {
                "red": ColorsRGB.RED.value,
                "green": ColorsRGB.GREEN.value,
                "black": ColorsRGB.BLACK.value,
            },
            "colors_hex": {
                "red": ColorsHEX.RED.value,
                "green": ColorsHEX.GREEN.value,
                "black": ColorsHEX.BLACK.value,
            },
        }
        return render(request, "habit_tracker/habits.html", context=context)


def update_habit(request):
    if is_ajax(request) and request.method == "POST":
        habit_request_data = HabitsViewDataExtractor(request.user.id).get_habit_data_from_request_body(request.body)

        habit_track_object = HabitTrack.objects.filter(
            habit_date=habit_request_data.date, habit__habit_name=habit_request_data.name, habit__user=request.user.id
        ).first()

        if not habit_track_object:
            habit_object = Habit.objects.filter(user=request.user.id, habit_name=habit_request_data.name).first()
            habit_track_object = HabitTrack(
                habit=habit_object, habit_date=habit_request_data.date, habit_done=habit_request_data.value
            )
        else:
            habit_track_object.habit_done = habit_request_data.value

        habit_track_object.save()

        return render(request, "habit_tracker/habits.html")
