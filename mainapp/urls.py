from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("colleges/", views.colleges, name="colleges"),
    path("students/", views.students, name="students"),
    path("address/", views.address, name="address"),
    path('contactus/',views.send_email, name='send_email'),
    path('emailsent/',views.emailsent,name='emailsent'),
    path('createadmin/', views.create_admin,name='create_admin'),
]
