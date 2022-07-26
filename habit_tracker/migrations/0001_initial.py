# Generated by Django 4.0.6 on 2022-07-26 16:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("habit_name", models.CharField(max_length=50)),
                ("habit_description", models.CharField(default="", max_length=200)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name="HabitTrack",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("habit_date", models.DateField()),
                ("habit_done", models.BooleanField()),
                ("habit", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="habit_tracker.habit")),
            ],
        ),
        migrations.AddConstraint(
            model_name="habit",
            constraint=models.UniqueConstraint(fields=("user", "habit_name"), name="user_habit"),
        ),
    ]
