from django.shortcuts import render,redirect

from .forms import EventForm
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
# Create your views here.
from .models import Event,Participation
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required
from Person.models import Person

def hello(request,name):
    
    msg ="lefri9i ya dawla aaa"
    
    
    return render(request,"event/bonjour.html",{ 'ca':msg , "nom":name})


def listEvent(request):
    
   eventList= Event.objects.all()
   
   
   
   
#    eventList= Event.objects.filter(state=True)

   return render(request,"event/list.html",{"events":eventList}) 

class DisplayEvents(ListView):
    model = Event
    template_name="event/list.html"
    context_object_name="events"
    
    def get_queryset(self):
        # eventList= Event.objects.filter(state=True).order_by('-evt_date')
        eventList= Event.objects.all()

        return eventList

class DetailsEvent(DetailView):
    model=Event
    template_name="event/details.html"  
    context_object_name ="event" 

def detailsEvent(request,ide):
    
    event = Event.objects.get(id=ide)
    
    person = request.user
    button=False
    
    participants= Participation.objects.filter(event=event,person=person)
    
    if participants:
        button=True
    else:
        button=False
        
        
    context={
        "event":event,
        "button":button
    }
    
    return render(request,"event/details.html",context) 


@login_required
def addEvent(request):
    form = EventForm()
    
    if request.method =="POST":
        
        form = EventForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.instance.organisateur = request.user
            form.save()
        
        return redirect("list")
      
        
    
    
    return render(request,"event/add.html",{'form':form})



class AddEventClass(LoginRequiredMixin,CreateView):
    
    model=Event
    template_name="event/add.html"
    form_class = EventForm
    success_url= "/list"
    
    
    
    
class Delete(DeleteView):
    model=Event
    template_name="event/delete.html"
    success_url="/event/list"
    
    


class UpdateEvent(UpdateView):
    
    model=Event
    form_class=EventForm
    template_name="event/update.html"
    success_url= "/event/list/"
    

def deleteEvent(request,idEvent):
  e1=  Event.objects.get(id=idEvent)
  if e1:
      e1.delete()
      return redirect("list")
  
  
  

def participer(request,ide):
    
    e1 = Event.objects.get(id=ide)
    p1 = request.user
    
    participant = Participation.objects.create(person=p1, event=e1)
    
    if participant:
            participant.save()
            e1.nbr_participant+=1
            e1.save()
            return redirect("list")
        
  
  
def cancel(request,ide):
    
    e1 = Event.objects.get(id=ide)
    p1 = request.user
    
    participant = Participation.objects.filter(person=p1, event=e1)
    
    if participant:
            participant.delete()
            e1.nbr_participant-=1
            e1.save()
            return redirect("list")