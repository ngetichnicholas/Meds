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
  path('patients', app_views.patients,name='patients'),
  path('update_patient/<int:patient_id>', app_views.update_patient,name='update_patient'),
  path('delete_patient/<int:patient_id>', app_views.delete_patient,name='delete_patient'),

  path('add_appointment', app_views.add_appointment,name='add_appointment'),
  path('appointments', app_views.appointments,name='appointments'),
  path('update_appointment/<int:appointment_id>', app_views.update_appointment,name='update_appointment'),
  path('delete_appointment/<int:appointment_id>', app_views.delete_appointment,name='delete_appointment'),

  path('add_prescription', app_views.add_prescription,name='add_prescription'),
  path('prescriptions', app_views.prescriptions,name='prescriptions'),
  path('update_prescription/<int:prescription_id>', app_views.update_prescription,name='update_prescription'),
  path('delete_prescription/<int:prescription_id>', app_views.delete_prescription,name='delete_prescription'),

  path('add_drug', app_views.add_drug,name='add_drug'),
  path('drugs', app_views.drugs,name='drugs'),
  path('update_drug/<int:drug_id>', app_views.update_drug,name='update_drug'),
  path('delete_drug/<int:drug_id>', app_views.delete_drug,name='delete_drug'),

  path('add_health_history', app_views.add_health_history,name='add_health_history'),
  path('history', app_views.history,name='history'),
  path('update_history/<int:history_id>', app_views.update_history,name='update_history'),
  path('delete_history/<int:history_id>', app_views.delete_history,name='delete_history'),

  path('add_feedback', app_views.add_feedback,name='add_feedback'),
  path('feedback', app_views.feedback,name='feedback'),
  path('update_feedback/<int:feedback_id>', app_views.update_feedback,name='update_feedback'),
  path('delete_feedback/<int:feedback_id>', app_views.delete_feedback,name='delete_feedback'),

  path('add_visit', app_views.add_visit,name='add_visit'),
  path('visits', app_views.visits,name='visits'),
  path('update_visit/<int:visit_id>', app_views.update_visit,name='update_visit'),
  path('delete_visit/<int:visit_id>', app_views.delete_visit,name='delete_visit'),
]