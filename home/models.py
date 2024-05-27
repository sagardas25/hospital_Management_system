from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/DoctorPic/',null = True,blank = True)
    address = models.CharField(max_length=35)
    mobile = models.CharField(max_length=15,null=True)

    @property
    def get_name(self):
        return self.user.first_name+ " " + self.user.last_name
    
    @property
    def get_id(self):
        return self.user.id 
    
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.user.username)





class Patient(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/patientPic/', null = True,blank = True)
    address = models.CharField(max_length=35)
    mobile = models.CharField(max_length=15,null=True)

    @property
    def get_name(self):
        return self.user.first_name+ " " + self.user.last_name
    
    @property
    def get_id(self):
        return self.user.id
    
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.user.username)
    
