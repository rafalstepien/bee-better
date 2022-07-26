from django.contrib import admin
from habit_tracker.models import Habit, HabitTrackerUser

admin.site.register(Habit)
admin.site.register(HabitTrackerUser)
