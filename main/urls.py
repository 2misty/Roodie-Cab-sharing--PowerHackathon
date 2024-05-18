# sharing/urls.py
from django.urls import path
from .views import register
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('register/', register, name='register'),
    path('admin/', admin.site.urls),
    path('sharing/', include('sharing.urls')),
]
