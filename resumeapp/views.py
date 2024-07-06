from django.shortcuts import render, redirect
from  django.http import  HttpResponse

from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Message

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Message

def send_message(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        receiver_username = request.POST.get('receiver')
        receiver = User.objects.get(username=receiver_username)
        sender = request.user if request.user.is_authenticated else None  # Handle anonymous sender
        Message.objects.create(sender=sender, receiver=receiver, content=content)
        return redirect('inbox')
    users = User.objects.exclude(username=request.user.username) if request.user.is_authenticated else User.objects.all()
    return render(request, 'send_message.html', {'users': users})

def inbox(request):
    if request.user.is_authenticated:
        messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    else:
        messages = []  # Anonymous users have no messages
    return render(request, 'inbox.html', {'messages': messages})




def index(request):
        return render(request,"index.html")
def resume(request):
        # return HttpResponse("kdkkkkkkkkk")
        return  render(request,"requestt.html")
def register (request):
    if request.method=="POST":
        username=request.POST['username']
        # first_name = request.POST['first_name']
        # last_name=request.POST['last_name']
        # email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name Taken")
                return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, "email already taken")
            #     return redirect('register')
            else:

                user=User.objects.create_user(username=username,password=password)
                # first_name = first_name, last_name = last_name, email = email
                user.save();
                return redirect('login')

        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('login')
    return  render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            # return redirect('/')
            # return redirect('')
            return render(request, "components.html")
        else:
            messages.info(request,"invalid credentials")
            return  redirect('login')
    return  render(request,"login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')