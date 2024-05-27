from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns =[

    path('', views.home_view, name='' ),
    path('admin_page/',views.admin_page),
    path('patientPage/',views.patient_page),
    path('doctorPage/',views.doctor_page),
    path('adminSign',views.admin_signin,name='adminSignIn'),
    path('doctorSign',views.doctor_signin,name='doctorSignIn'),
    path('patientSign',views.patient_signin,name='patientSignIn'),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html')),
    path('doctorlogin', LoginView.as_view(template_name='doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='patientlogin.html')),
    path('afterlogin', views.afterlogin,name='afterlogin'),
    path('afterlogin/', views.afterlogin,name='afterlogin'),
    path('logout',views.logout_user, name='logout'),
    path('accounts/profile/',views.profile),
 
]