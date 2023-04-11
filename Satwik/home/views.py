from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# Create your views here.

class HomeView(TemplateView):
  template_name = 'home/welcome.html'
class AuthView(LoginRequiredMixin,TemplateView):
  template_name = 'home/auth.html'
  login_url = '/admin'

class LoginView(TemplateView):
  template_name = 'home/login.html'
class RegisterView(TemplateView):
  template_name = 'home/register.html'
