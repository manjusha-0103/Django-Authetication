
#from sre_constants import SUCCESS
from django.conf import settings
from django.shortcuts import redirect, render
'''from django.http import HttpResponse
from django.contrib import messages
from django.db import IntegrityError, models, router, transaction'''
from . forms import Registerform



# Create your views here.

def register(response):
    if response.method == "POST":
        form = Registerform(response.POST)
        if form.is_valid():
            form.save()
        return redirect(settings.LOGIN_REDIRECT_URL)
    else :        
        form = Registerform()
    return render(response,"registration/registration.html",{"form" : form})