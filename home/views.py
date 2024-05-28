from django.shortcuts import render,redirect
from . import models, forms 
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import login,logout , authenticate
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.cache import never_cache



# view for home
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('afterlogin'))
    return render(request, 'home.html')




# view for patient register/login option page

def patient_page(request,user_type):
    if request.user.is_authenticated:
         return HttpResponseRedirect('afterlogin')
    return render(request, 'basePage.html' , {'user_type': user_type})


def doctor_page(request,user_type):
    if request.user.is_authenticated:
         return HttpResponseRedirect('afterlogin')
    return render(request, 'basePage.html' , {'user_type': user_type})


# def patient_page(request):
#     if request.user.is_authenticated:
#          return HttpResponseRedirect('afterlogin')
#     return render(request, 'patient_page.html' )


# def doctor_page(request):
#     if request.user.is_authenticated:
#             return HttpResponseRedirect('afterlogin')
#     return render(request, 'doctor_page.html')




# view for doctor registration page

def doctor_signin(request , user_type):
     

     if request.user.is_authenticated:
        HttpResponseRedirect(reverse('doctor_dash'))
     
     if request.method == 'POST':
          user_form = forms.CustomUserCreation(request.POST)
          doctor_form =forms.doctorForm(request.POST,request.FILES)

          if user_form.is_valid() and doctor_form.is_valid():
               
               new_user = user_form.save()
               new_user.set_password(new_user.password)
               new_user.save()

               doctor = doctor_form.save(commit=False)
               doctor.user = new_user
               doctor = doctor.save()


               doctor_group = Group.objects.get_or_create(name='DOCTOR')
               doctor_group[0].user_set.add(new_user)

               return HttpResponseRedirect('doctorlogin')
          
          

     else: 

        user_form = forms.CustomUserCreation()
        doctor_form =forms.doctorForm()

     contxt = { 'user_form' : user_form , 'doctor_form': doctor_form , 'user_type': user_type }
     return render(request,'signinBase.html', context=contxt)






# patient sign in view

def patient_signin(request , user_type):
       
     if request.user.is_authenticated:
          HttpResponseRedirect(reverse('patient_dash'))
     
     if request.method == 'POST':
          user_form = forms.CustomUserCreation(request.POST)
          patient_form = forms.patientForm(request.POST,request.FILES)

          if user_form.is_valid() and patient_form.is_valid():
               
               new_user = user_form.save()
               new_user.set_password(new_user.password)
               new_user.save()

               patient = patient_form.save(commit=False)
               patient.user = new_user
               patient = patient.save()

               doctor_group = Group.objects.get_or_create(name='PATIENT')
               doctor_group[0].user_set.add(new_user)

               return HttpResponseRedirect('patientlogin')
          
          
     else: 

        user_form = forms.CustomUserCreation()
        patient_form = forms.patientForm()

     contxt = { 'user_form' : user_form ,'patient_form' : patient_form  , 'user_type': user_type}
     return render(request,'signinBase.html', context=contxt)
     



# log in view for patient

def patient_login(request, user_type):
     
     if request.user.is_authenticated:
          HttpResponseRedirect(reverse('patient_dash'))

     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username , password=password)

        if user is not None :
             login(request,user)
             return render(request,'patient-dashboard.html')
        else:
             messages.error(request, "Invalid credentials")

     
     return render(request,'patientlogin.html' ,{'user_type': user_type})



# log in view for doctor
def doctor_login(request,user_type):
     
     if request.user.is_authenticated:
          HttpResponseRedirect(reverse('doctor_dash'))
          
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username , password=password)

        if user is not None :
             login(request,user)
             return render(request,'doctor-dashboard.html')
        else:
             messages.error(request, "Invalid credentials")

     return render(request,'doctorlogin.html',{'user_type': user_type} )
          
  

# boolean check for user

def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()



# this is login page_view
# this is used to keep user logged when user again opens the homepage after closing it

@login_required
def afterlogin(request):
     
     if is_doctor(request.user):
          return render(request,'doctor-dashboard.html')     
    
     
     elif is_patient(request.user):
         return render(request,'patient-dashboard.html')
        
     
     else:
          return HttpResponse(" May be super user is logged in , Log out from there")



# view for logout
def logout_user(request):
    logout(request)
    return redirect('')



# had to create this bcoz server was automatically getting redirected to this url ('account/profile/') 
@login_required
@never_cache
def profile(request):
    
    if is_doctor(request.user):
          return render(request,'doctor-dashboard.html')
     
    elif is_patient(request.user):
         return render(request,'patient-dashboard.html')
               


@login_required   
def doctor_dash(request):
      return render(request,'doctor-dashboard.html')

@login_required
def patient_dash(request):
      return render(request,'patient-dashboard.html')






