from django.urls import path
from .views import HomePageView
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView

name_app = 'general'
 
 
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', LoginView.as_view(template_name='home.html'), name='login'),
]