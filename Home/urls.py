from django.urls import path,include
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('About/', views.about, name='about'),
     path('Contact/', views.contact, name='contact'),
     path('Search/', views.search,name='search'),
   
]

