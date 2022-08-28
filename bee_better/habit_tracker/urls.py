from django.urls import path

from .views.views import habits, index, update_habit

urlpatterns = [
    path("", index, name="index"),
    path("habits/", habits, name="habits"),
    path("update_habit/", update_habit, name="update_habit"),
]
