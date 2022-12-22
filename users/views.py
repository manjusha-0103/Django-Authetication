
#from sre_constants import SUCCESS
from email import message
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError, models, router, transaction
from . forms import Registerform



# Create your views here.

def register(response):
    if response.method == "POST" :
        username = response.POST["username"]
        email = response.POST["email"]
        password1 = response.POST["pswd1"]
        password2 = response.POST["pswd2"]

        try:    
            myuser = User.objects.create_user(username, email, password1)
            myuser.password2 = password2
        
            myuser.save()
            #if myuser.objects.filter :
            if len(username) >10:
                messages.error(response,"Username should contain at most 10 characters.")
        except IntegrityError:
            pass
        messages.success(response,"You have successfully registered.")
        return redirect('login')
      
    return render(response,'registration/registration.html')
    '''if response.method == "POST":
        form = Registerform(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response,"You have registered successfully!")
            return redirect('login')
        else :
            if form.cleaned_data.get("password1" )!= form.cleaned_data.get("password2" ):
                messages.error(response,"Password is not matching...")
            elif form.cleaned_data.get("username" )[len(form.cleaned_data.get("username" ))-4:] != ".com":
                messages.error(response,"Add correct email..")
            else :
                return redirect('login')  

    else :        
        form = Registerform()
        print(form)

        return render(response,"registration/registration.html",{"form" : form})'''

def login_view(request):
    if request.method == "POST" :
        username  = request.POST.get('username')
        password = request.POST.get('password1')
        print(username)
        _user = authenticate(username = username ,password = password)
        print(_user)
        if _user is not None :
            login(request,_user)
            messages.success(request,"You have logged in successfully .......")
            return redirect('home')
        else :
            messages.error(request,"Wrong credentials")    
            return redirect('login')
    return render(request,'registration/login.html')

    '''if request.method == 'POST':
        username  = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request,usernmae = username ,password = password)
        if user == None :
            messages.error(request,"Username or password is incorrect.")
            return render(request,"registration/login.html")
        else :
            login(request,user)
            messages.success(request,"You have loged in successfully.")
            return redirect('/')
    else :            
        return render(request,"registration/login.html")'''

def logout_view(request):
    logout(request)
    messages.success(request,"You have successfully logout!")
    #return redirect("logout")
        
    return render(request,"registration/signout/signout.html")    

def reset_password(request):
    '''if request.method == "POST":
        reset_pass = request.get()'''
    return render(request,"template/registration/reset_pass.html")     