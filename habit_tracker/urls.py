from django.urls import path

from .views.views import add_habit, habits, index, login_user, logout_user, register, remove_habit, update_habit

urlpatterns = [
    path("", index, name="index"),
    path("habits/", habits, name="habits"),
    path("update_habit/", update_habit, name="update_habit"),
    path("add_habit/", add_habit, name="add_habit"),
    path("remove_habit/", remove_habit, name="remove_habit"),
    path("login_user/", login_user, name="login_user"),
    path("register/", register, name="register"),
    path("logout_user/", logout_user, name="logout_user"),
]
