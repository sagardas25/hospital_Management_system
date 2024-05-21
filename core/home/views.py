from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *





def home(request):
    
    return render(request,'home.html')


def login_page(request):


    # if user submits the form 

    if request.method == "POST" :

        username = request.POST.get('username')
        password = request.POST.get('password')

        # checking if username already  exits or not 

        if not User.objects.filter(username=username).exists() :

            messages.error(request,'Invalid username')
            return redirect('/login/')
        
 
        # tries to authenticate passwrd and username reurns None on failure

        user = authenticate(username = username , password = password)


        if user is None : 

            messages.error(request ,'Invalid password')
            return redirect('/login/')
        
        else :
            login(request,user)
            return render('/home/')
        

    # renders login ui     
    return render(request,'login.html')  



def register_page(request) :
        
        # if user submits the form 
                 
        if request.method == "POST" :
             
            Username = request.POST.get('username')
            password = request.POST.get('password')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')


             # checking if username already exists

            if not User.objects.filter(Username=Username).exits():
             
                messages.error(request,'Invalid username')
                return redirect('/register/')
             

            # creating a new user with given information
            user = User.objects.create_user (

                first_name = first_name,
                last_name = last_name,
                username= Username      )
        
            # setting the passwords
            user.set_password(password)
            user.save()



             # now displaying the successfully registered message

            messages.info(request,"Account created successfully !")
            return redirect('/login/')



        # renders the registration ui
        return render(request,'register.html')




