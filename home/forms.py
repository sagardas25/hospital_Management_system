from django import forms
from django.contrib.auth.models import User
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.forms import Form  
from django.contrib import messages





#doctor forms
# class doctorSigninForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username','password']
#         widgets = {

#             'password' : forms.PasswordInput()
#         }   


class CustomUserCreation(UserCreationForm):
    first_name = forms.CharField(label='first name', min_length=3, max_length=25)
    last_name = forms.CharField(label='last name', min_length=3, max_length=25)
    username = forms.CharField (label='username', min_length=5,max_length=150)
    # password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    # password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']

        widgets = {

            'password1' : forms.PasswordInput(),
            'password2'  : forms.PasswordInput()

            }

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new =  User.objects.filter(username=username)

        if new.count():
            raise forms.ValidationError( "User already Exist")
        
        return username
    

    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2'] 

        if password1 and password2 and password1 != password2 :
            raise forms.ValidationError("password don't match")
        
        return password2
    

    def save(self, commit = True):
        user = User.objects.create_user(

            self.cleaned_data['username'],
            self.cleaned_data['password1']

         )

        return user




class doctorForm(forms.ModelForm):
    class Meta:
        model = models.Doctor
        fields = ['address','mobile','profile_pic']




#patient forms

# class patientSigninForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['first_name','last_name','username','password']
#         widgets = {

#             'password' : forms.PasswordInput()
#         }   


class patientForm(forms.ModelForm):
    class Meta:
        model = models.Patient 
        fields = ['address','mobile','profile_pic']


