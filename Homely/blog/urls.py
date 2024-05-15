from django.urls import path
from .views import HomePageView

name_app = 'blog'
 
 
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]