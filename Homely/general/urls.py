from django.urls import path
from .views import HomePageView

name_app = 'general'
 
 
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]