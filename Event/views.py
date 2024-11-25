from django.shortcuts import render,redirect

from .forms import EventForm
from django.views.generic import ListView,DetailView,CreateView
# Create your views here.
from .models import Event

def hello(request,name):
    
    msg ="lefri9i ya dawla aaa"
    
    
    return render(request,"event/bonjour.html",{ 'ca':msg , "nom":name})


def listEvent(request):
    
#    eventList= Event.objects.all()
   
   eventList= Event.objects.filter(state=True)

   return render(request,"event/list.html",{"events":eventList}) 

class DisplayEvents(ListView):
    model = Event
    template_name="event/list.html"
    context_object_name="events"
    
    def get_queryset(self):
        # eventList= Event.objects.filter(state=True).order_by('-evt_date')
        eventList= Event.objects.filter(state=True)

        return eventList

class DetailsEvent(DetailView):
    model=Event
    template_name="event/details.html"  
    context_object_name ="event" 

def detailsEvent(request,ide):
    
    event = Event.objects.get(id=ide)
    
    
    return render(request,"event/details.html",{"event":event}) 



def addEvent(request):
    form = EventForm()
    
    if request.method =="POST":
        
        form = EventForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
        
        return redirect("list")
      
        
    
    
    return render(request,"event/add.html",{'form':form})



class AddEventClass(CreateView):
    
    model=Event
    template_name="event/add.html"
    form_class = EventForm
    success_url= "/list"