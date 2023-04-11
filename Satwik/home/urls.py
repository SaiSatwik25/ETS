from django.urls import path

from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('auth', views.AuthView.as_view(),name='auth'),
    # path('aboutus',views.AboutView.as_view(), name='aboutus'),
    path('login',views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),

]
