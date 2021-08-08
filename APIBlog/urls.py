from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/v1/', include('api.urls')),
]
