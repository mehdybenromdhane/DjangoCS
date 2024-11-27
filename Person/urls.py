from django.urls import path

from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', register ,name="register"),
    path('logout/',LogoutView.as_view() , name="logout"),
    path('login/',login_user,name="login")
   


]