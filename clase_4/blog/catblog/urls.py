from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.newpost),
    path('view/', views.viewpost),
    path('edit/', views.editpost),
    path('delete/', views.deletepost),
]