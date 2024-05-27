from django import forms
from django.contrib.auth.models import User
from . import models


#admin sign in
class adminSigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password']
        widgets = {

            'password' : forms.PasswordInput()
        }



#doctor forms
class doctorSigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password']
        widgets = {

            'password' : forms.PasswordInput()
        }   

class doctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['address','mobile','profile_pic']



#patient forms

class patientSigninForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password']
        widgets = {

            'password' : forms.PasswordInput()
        }   


class patientForm(forms.ModelForm):
    class Meta:
        model = models.Patient 
        fields = ['address','mobile','profile_pic']


