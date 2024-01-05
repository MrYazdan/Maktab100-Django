from .forms import SignupForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import HttpResponseForbidden
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, View


class Login(LoginView):
    template_name = "login.html"


count_of_logout = {}


class Logout(View):
    def get(self, request):
        if self.request.user:
            print(request.COOKIES)

            latest_user_login = request.user.email
            logout(request)
            count_of_logout[latest_user_login] = count_of_logout.get(latest_user_login, 0) + 1
            response = redirect('home')
            response.set_cookie('latest_user_login', latest_user_login)
            response.set_cookie('count_of_logout', count_of_logout[latest_user_login])
            return response


class Signup(CreateView):
    form_class = SignupForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"
