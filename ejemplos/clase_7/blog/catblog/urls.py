from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/new', views.newpost, name='create_post'),
    path('post/view', views.viewpost, name='view_post'),
    path('post/edit', views.editpost, name='edit_post'),
    path('post/delete', views.deletepost, name='delete_post'),
]