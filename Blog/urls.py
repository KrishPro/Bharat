from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog, name='blog'),
    path('Add/', views.Add, name='Add'),

    path('Posts/<str:Sno>', views.Post, name='post'),
]