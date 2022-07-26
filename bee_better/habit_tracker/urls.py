from django.urls import path

from .views.views import habits, index

urlpatterns = [
    path("", index, name="index"),
    path("habits/", habits, name="habits"),
]
