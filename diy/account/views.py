from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import auth
# Create your views here.

def register(request):
    if request.method=="POST":
        user_name=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['confirmPassword']

        if password==c_password:

            if User.objects.filter(email=email).exists() or  User.objects.filter(username=user_name).exists():
                print("username or password taken")
                return redirect('message', title="Info", message="Already registered !")
            else:

                user=User.objects.create_user(username=user_name,email=email,password=password)
                user.save()
                print("user created")
                return redirect('/') 
        else:
            messages.error(request,"Password do not match")
            return redirect('message', title="error", message="Password not match")
    else:
        return render(request,"register.html")

def login_page(request):
    if request.method=='POST':
   
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user is not None:
            print("hi")
            login(request,user)
            return redirect('project_list')

    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

