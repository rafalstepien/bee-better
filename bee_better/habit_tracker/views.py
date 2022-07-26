from django.shortcuts import render


def index(request):
    return render(request, "habit_tracker/index_page.html")


def habits(request):
    return render(request, "habit_tracker/habits.html")
