from django.urls import path
from .views import RegisterView, ConfirmView, LoginView

urlpatterns = [
    path("v1/users/register/", RegisterView.as_view(), name="register"),
    path("v1/users/confirm/", ConfirmView.as_view(), name="confirm"),
    path("v1/users/login/", LoginView.as_view(), name="login"),
]
