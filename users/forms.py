
from tkinter import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django import forms 
from django.contrib.auth.models import User


class Registerform(UserCreationForm):
    email =  forms.EmailField()
    class Meta  :
        model = User
        fields = ['username','email','password1','password2']
        Widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;max-height:50px; ',
                'placeholder': 'username'
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
                  
        }

