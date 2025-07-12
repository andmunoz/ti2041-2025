from django.urls import path
from .app import api

urlpatterns = [
    path('v1/', api.urls),
]