from django.shortcuts import render,redirect

from django.contrib.auth.models import auth,User
from django.contrib.auth import authenticate
from .models import  user_details


# Create your views here.


def index(request):
    print(request.user)
    if request.user.is_anonymous:
        return render(request,'pulse/index.html')
    elif(request.user.is_superuser):
        auth.logout(request)
        return redirect('/')
    else:
        username=request.user
        return render(request, 'pulse/main.html',{'username':username})


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if len(user_details.objects.filter(username=username,password=password))==1:
                auth.login(request, user)
        return redirect('/')

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        new_user=user_details(username=username,password=password)
        new_user.save()
        user = User.objects.create_user(username=username, password=password)
        user.save()
        user_access=authenticate(username=username,password=password)
        auth.login(request,user)
        return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')


def chatbox(request):

    return render(request,'pulse/chatarea.html')




