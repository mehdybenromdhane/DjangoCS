from django.shortcuts import render,redirect

from .forms import UserRegisterForm
from django.contrib.auth import login,authenticate
# Create your views here.

def register(request):
    
    form = UserRegisterForm()
    
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        
        if form.is_valid():
            user=form.save()
            login(request ,user)
            
            
    
    
    return render(request,"person/register.html", {"form":form})



def login_user(request):
    
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username,password=password)
        
        if user:
            login(request,user)
            return redirect('list')
        
        else:
            return redirect('login')
        
    
    return render(request,'person/login.html',{})
    