from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        DOCTOR = "DOCTOR", 'Doctor'
        PATIENT = "PATIENT", 'Patient'
   

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices, default=base_role)

    def save(self, *args, **kwargs):
        if not self.pk: 
            self.role = self.base_role
        super().save(*args, **kwargs)


    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )


class Doctors(User):
    
    base_role=User.Role.DOCTOR

    class Meta:
        proxy=True
    
    def Welcome(self):
        return "only for doctors"
    

class Patients(User):
    
    base_role=User.Role.PATIENT

    class Meta:
        proxy=True
    
    def Welcome(self):
        return "only for patient"
    

