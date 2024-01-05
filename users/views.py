from .forms import SignupForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponseForbidden
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, View


class Login(LoginView):
    template_name = "login.html"


class Logout(View):
    def get(self, request):
        if self.request.user:
            logout(request)
            return redirect('home')


class Signup(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
