from django.urls import path
from . import views

urlpatterns = [
    
     path('Login/',views.Login,name="login"),
     path('Profile/',views.Profile,name="Profile"),
     path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
     path('ChangeInformation/',views.ChangeInformation,name="ChangeInformation"),
     path('Logout/',views.LogOut,name="logout"),
     path('Signup/',views.signup,name='Signup')
]

