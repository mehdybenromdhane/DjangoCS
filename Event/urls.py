from django.urls import path

from .views import *


urlpatterns = [
    path('hello/<str:name>', hello ),
    path('list/',listEvent , name="list"),
    path('details/<int:ide>',detailsEvent , name="details") 

]