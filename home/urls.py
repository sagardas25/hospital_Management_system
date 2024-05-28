from django.urls import path
from . import views 
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns =[

    path('', views.home_view, name='' ),
    # path('patientPage/<str:user_type>/',views.patient_page,name='patient_page'),
    # path('doctorPage/<str:user_type>/',views.doctor_page,name='doctor_page'),
    path('patientPage/',views.patient_page,{'user_type': 'patient'},name='patient_page'),
    path('doctorPage/',views.doctor_page,{'user_type': 'doctor'},name='doctor_page'),
    path('doctorSign',views.doctor_signin, {'user_type': 'doctor'} , name='doctorSignIn'),
    path('patientSign',views.patient_signin,{'user_type': 'patient'}, name='patientSignIn'),
    path('doctorlogin', views.doctor_login ,{'user_type': 'doctor'}),
    path('patientlogin', views.patient_login,{'user_type': 'patient'}),
    path('afterlogin', views.afterlogin,name='afterlogin'),
    path('afterlogin/', views.afterlogin,name='afterlogin'),
    path('logout',views.logout_user, name='logout'),
    path('accounts/profile/',views.profile),

    path('doctor_dashboard/',views.doctor_dash,name='doctor_dash'),
    path('patient_dashboard/',views.patient_dash , name='patient_dash'),

    path('adminlogin', LoginView.as_view(template_name='adminlogin.html')),
 
]