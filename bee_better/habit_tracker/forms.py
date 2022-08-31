from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]



class AddHabitForm(forms.Form):
    habit_name = forms.CharField(label='Habit name', max_length=100)
