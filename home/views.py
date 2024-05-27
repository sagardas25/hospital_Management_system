from django.shortcuts import render,redirect
from . import models, forms
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth import login,logout
from django.urls import reverse
from django.contrib import messages


# view for home
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'home.html')


# view for admin register/login option page

def admin_page(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    
    return render(request, 'admin_page.html' )


# view for patient register/login option page

def patient_page(request):
    if request.user.is_authenticated:
         return HttpResponseRedirect('afterlogin')
    return render(request, 'patient_page.html' )


#view for doctor register/login option page 

def doctor_page(request):
    if request.user.is_authenticated:
            return HttpResponseRedirect('afterlogin')
    return render(request, 'doctor_page.html')



## view for admin registration page

def admin_signin(request):

    if request.method == 'POST':
          form = forms.adminSigninForm(request.POST)
          if form.is_valid():
               user = form.save()
               user.set_password(user.password)
               user.save()
               admin_group = Group.objects.get_or_create(name = 'ADMIN')
               admin_group[0].user_set.add(user)
               return HttpResponseRedirect('adminlogin')
          
          
    else :
        form = forms.adminSigninForm()

    return render(request, 'adminSignin.html',{'form':form})



# view for doctor registration page

def doctor_signin(request):
     
     if request.method == 'POST':
          user_form = forms.doctorSigninForm(request.POST)
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

        user_form = forms.doctorSigninForm()
        doctor_form =forms.doctorForm()

     contxt = { 'user_form' : user_form , 'doctor_form': doctor_form }
     return render(request,'doctorsignin.html',context=contxt)





def patient_signin(request):
     
     if request.method == 'POST':
          user_form = forms.patientSigninForm(request.POST)
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

        user_form = forms.patientSigninForm()
        patient_form = forms.patientForm()

     contxt = { 'user_form' : user_form ,'patient_form' : patient_form }
     return render(request,'patientsignup.html',context=contxt)
     

# boolean check for user

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()
def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()



# this is login page_view

@login_required
def afterlogin(request):
     
     if is_admin(request.user):
          return render(request,'admin-dashboard.html')
     
     elif is_doctor(request.user):
          return render(request,'doctor-dashboard.html')
     
     elif is_patient(request.user):
         return render(request,'patient-dashboard.html')
     
     
     else:
          return HttpResponse(" May be super user is logged in , Log out from there")




# view for logout

def logout_user(request):
    logout(request)
    return redirect('')


 


@login_required
def profile(request):
    
    if is_admin(request.user):
          return render(request,'admin-dashboard.html')
     
    elif is_doctor(request.user):
          return render(request,'doctor-dashboard.html')
     
    elif is_patient(request.user):
         return render(request,'patient-dashboard.html')
               
     
@login_required
def doctor_dashboard(request):
    if not request.user.is_doctor():
        return redirect('login')
    return render(request, 'doctor_dashboard.html')

@login_required
def patient_dashboard(request):
    if not request.user.is_patient():
        return redirect('login')
    return render(request, 'patient_dashboard.html')





