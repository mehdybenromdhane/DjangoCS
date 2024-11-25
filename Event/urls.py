from django.urls import path

from .views import *


urlpatterns = [
    path('hello/<str:name>', hello ),
    path('list/',listEvent , name="list"),
    path('details/<int:ide>',detailsEvent , name="details") ,
    path('display/', DisplayEvents.as_view()),
    path('displayById/<int:pk>',DetailsEvent.as_view()),
    path('add/',addEvent, name="addEvent"),
    path('addEvent/',AddEventClass.as_view(), name="addEventClass")


]