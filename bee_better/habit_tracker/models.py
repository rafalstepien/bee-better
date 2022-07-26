import datetime

from django.db import models


class Habit(models.Model):
    habit_name: str = models.CharField(max_length=100)
    habit_date: datetime.date = models.DateField()
    habit_done: bool = models.BooleanField()


class HabitTrackerUser(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
