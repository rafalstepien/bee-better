from django.urls import path

from .views.views import habits, index, login_user, logout_user, register, update_habit

urlpatterns = [
    path("", index, name="index"),
    path("habits/", habits, name="habits"),
    path("update_habit/", update_habit, name="update_habit"),
    path("login_user/", login_user, name="login_user"),
    path("register/", register, name="register"),
    path("logout_user/", logout_user, name="logout_user"),
]
