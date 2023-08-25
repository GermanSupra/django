from django.urls import path

from .views import logout_view, profile_view, login_view

urlpatterns = [
    path("profile/", profile_view, name="profile"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name='logout')
]
