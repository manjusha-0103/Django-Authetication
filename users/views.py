#from sre_constants import SUCCESS
from email import message
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import IntegrityError, models, router, transaction
#from . forms import Registerform
from django.views.generic.edit import DeleteView


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
      
    return render(response,'account/registration.html')
    

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
    return render(request,'account/login.html')

def logout_view(request):
    logout(request)
    messages.success(request,"You have successfully logout!")
    #return redirect("logout")
        
    return render(request,"account/signout/signout.html")    

def delete_account(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pswd1')
        
        #u = User.objects.filter(password=password).first()
        u = authenticate(username=username,password=password)
        print(u)  
        if u:
            u.delete()
            messages.success(request,"Account is deleted successfully.....")
            return redirect('home')
        else:
            messages.error(request,"Enter the correct data")
            return redirect('delete')    
        
    return render(request,"account/delete_profile.html")
    '''

    user = User.objects.get(id= user.pk)
    # You first logout the user then delete the account
    logout(request)
    # You can use either of these
    # To Soft Delete
    user.active = False
    user.save()
    # To Hard Delete
    user.delete()
    messages.success(request,"You account has been deleted Successfully!")
    return redirect('home')
    #model = User
    '''
    
def reset_password(request):
    if request.method == "POST":
        reset_pass = request.POst.get("password")
        User.password = reset_pass
        messages.success(request,"Password is reset")
    return render(request,"template/account/reset_pass.html")  

"""
def register(request):
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

def login_view(request) :
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

def         


"""
      