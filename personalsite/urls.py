
from django.urls import path
from personalsite import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('education/', views.education, name='education'),
    path('resume/', views.resume, name='resume'),
]