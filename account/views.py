from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Q
from course.models import Profile
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.
def login(request):
    print("inside Login")
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")
    else:
        return render(request,"login.html")
def logout(request):
    print("logout")
    auth.logout(request)
    return redirect("/")
@csrf_exempt
def register(request):
    print("registration")
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        email=request.POST["email"]
        profilepic=request.FILES["profilepic"]
        if User.objects.filter(Q(username=username)|Q(email=email)).exists():
            messages.info(request,"User already exist")
            return redirect("login")
        else:
            user=User.objects.create_user(username=username,password=password,email=email)
            user.save()
            profile=Profile.objects.create(profile_user=user,profile_rating=0,profile_pic=profilepic)
            profile.save
            return redirect("login")
    else:
        return render(request,"registration.html")