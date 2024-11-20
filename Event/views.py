from django.shortcuts import render

# Create your views here.
from .models import Event

def hello(request,name):
    
    msg ="lefri9i ya dawla aaa"
    
    
    return render(request,"event/bonjour.html",{ 'ca':msg , "nom":name})


def listEvent(request):
    
#    eventList= Event.objects.all()
   
   eventList= Event.objects.filter(state=True)

   return render(request,"event/list.html",{"list":eventList}) 


def detailsEvent(request,ide):
    
    event = Event.objects.get(id=ide)
    
    
    return render(request,"event/details.html",{"event":event}) 
