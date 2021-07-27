from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views as app_views
from django.contrib.auth import views as auth_views



urlpatterns = [
  path('', app_views.index, name="home"),
  path('accounts/login/',app_views.login,name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
  path('add_patient', app_views.add_patient,name='add_patient'),
  path('add_appointment', app_views.add_appointment,name='add_appointment'),
  path('add_prescription', app_views.add_prescription,name='add_prescription'),

]