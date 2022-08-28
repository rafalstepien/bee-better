import pytest
from habit_tracker.models import Habit
from django.contrib.auth.models import User


@pytest.fixture
def example_list_of_habits():
    return [
        Habit(user=User(), habit_name="habit_1"),
        Habit(user=User(), habit_name="habit_2"),
        Habit(user=User(), habit_name="habit_3"),
    ]


