from django.shortcuts import render

from .forms import UserRegisterForm
from django.contrib.auth import login
# Create your views here.

def register(request):
    
    form = UserRegisterForm()
    
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        
        if form.is_valid():
            user=form.save()
            login(request ,user)
            
            
    
    
    return render(request,"person/register.html", {"form":form})