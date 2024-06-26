"""
URL configuration for Homely project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import HomePageView
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView
from Homely import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('general/', include(('general.urls', 'general'))),
    path('admin/', admin.site.urls),
    path('registrar/', views.registrar, name='registrar'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='home.html'), name='logout'),
    path('catalogos/', include(('catalogos.urls', 'catalogos'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
