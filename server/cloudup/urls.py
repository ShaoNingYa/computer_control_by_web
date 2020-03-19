"""cloudup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url

from app_window_show.views import app_get_main
from app_window_show.views import get_new_pic
from app_window_show.views import push_position
from app_window_show.views import get_position

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', app_get_main),
    url(r'get_next_pic', get_new_pic),
    url(r'push_position', push_position),
    url(r'get_position', get_position),
]
