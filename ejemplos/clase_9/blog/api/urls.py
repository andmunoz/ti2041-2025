from django.contrib import admin
from django.urls import path, include
from .api import app

urlpatterns = [
    path('v1/', app.urls),
]