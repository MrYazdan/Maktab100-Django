from . import views
from django.views.generic import TemplateView
from django.urls import path, include

urlpatterns = [
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("signup/", views.Signup.as_view(), name="signup"),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
]
