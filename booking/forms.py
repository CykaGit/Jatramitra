from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from django.forms import ModelForm

class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']
        

class PassengerInfoFormset(forms.ModelForm):
    class Meta:
        model=PassengerInfo
        fields='__all__'

        
    def save(self, commit=True):
        instance = super().save(commit=False)
        # Additional processing or validation can be done here
        if commit:
            instance.save()
        return instance   


     