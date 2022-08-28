import datetime

from django.contrib.auth.models import User
from django.db import models
from pydantic import BaseModel


class Habit(models.Model):
    """
    Class responsible for modeling single habit with metadata.
    """

    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "habit_name"], name="user_habit")]

    user: str = models.ForeignKey(User, on_delete=models.CASCADE)
    habit_name: str = models.CharField(max_length=50)
    habit_description: str = models.CharField(max_length=200, default="")

    def __str__(self):
        return f"{self.habit_name.lower()} for {self.user.username}"


class HabitTrack(models.Model):
    """
    Class responsible for modeling habit history.
    """

    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    habit_date: datetime.date = models.DateField()
    habit_done: bool = models.BooleanField()

    def __str__(self):
        return f"Track of {self.habit}"


class AJAXRequestData(BaseModel):
    row_id: int
    column_id: int
    habit_value: bool
